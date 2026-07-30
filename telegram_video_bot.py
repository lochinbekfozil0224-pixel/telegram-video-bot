import os
import json
import logging
from datetime import datetime
from pathlib import Path
import asyncio
import aiohttp

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ChatMember
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters, ConversationHandler
from telegram.error import TelegramError
import yt_dlp
from PIL import Image, ImageDraw, ImageFont
import tempfile

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
ADMIN_ID = 8135915671
BOT_TOKEN = "7457477557:AAGUBa6qRiI1z67xgESMvWHJwC4bKHBNnCE"

# States for conversations
SETTING_CHANNEL, SETTING_SUPPORT, SETTING_WATERMARK, EDITING_USER = range(4)

# Default data structure
DEFAULT_CONFIG = {
    "bot_name": "VidoGo_Bot",
    "required_channels": [],
    "ads_channel": None,
    "support_channel": None,
    "watermark_text": "😀 Ushbu video juda ajoyib uni do'stlaringiz bilan ulashing!\n\nⓂ️ @VidoGo_Bot\nⓂ️ @XtraSMMUz",
    "block_downloads": False
}

class ConfigManager:
    """Manage bot configuration and user data"""
    
    def __init__(self, config_file="bot_config.json", users_file="users_data.json"):
        self.config_file = config_file
        self.users_file = users_file
        self.config = self.load_config()
        self.users = self.load_users()
    
    def load_config(self):
        if Path(self.config_file).exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return DEFAULT_CONFIG.copy()
    
    def load_users(self):
        if Path(self.users_file).exists():
            with open(self.users_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def add_user(self, user_id, username="Unknown"):
        self.users[str(user_id)] = {
            "username": username,
            "joined": datetime.now().isoformat(),
            "downloads": 0
        }
        self.save_users()
    
    def get_user_stats(self):
        return {
            "total_users": len(self.users),
            "downloads": sum(u.get("downloads", 0) for u in self.users.values())
        }

config_manager = ConfigManager()

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Check if user is subscribed to required channels"""
    user_id = update.effective_user.id
    
    # Skip check for admin
    if user_id == ADMIN_ID:
        return True
    
    for channel_id in config_manager.config.get("required_channels", []):
        try:
            member = await context.bot.get_chat_member(channel_id, user_id)
            if member.status not in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
                return False
        except TelegramError:
            continue
    
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command"""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    # Add user to database
    if str(user.id) not in config_manager.users:
        config_manager.add_user(user.id, user.username or "Unknown")
    
    # Check subscription
    if not await check_subscription(update, context):
        keyboard = []
        for i, channel_id in enumerate(config_manager.config.get("required_channels", [])):
            keyboard.append([InlineKeyboardButton(
                f"📺 Kanalga Obuna Bo'ling {i+1}",
                url=f"https://t.me/{str(channel_id).replace('-100', '')}"
            )])
        keyboard.append([InlineKeyboardButton("✅ Obuna Qildim", callback_data="check_sub")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "🔐 Video yuklab olish uchun, iltimos quyidagi kanalga obuna bo'ling:\n\n"
            "Please subscribe to the channel to download videos!",
            reply_markup=reply_markup
        )
        return
    
    # User is subscribed or admin
    if user.id == ADMIN_ID:
        await show_admin_menu(update, context)
    else:
        await update.message.reply_text(
            f"👋 Assalomu Aleykum {user.first_name}!\n\n"
            f"🎬 Video yuklash boti\n"
            f"📱 Instagram, YouTube, TikTok dan videolar yuklang!\n\n"
            f"Video linkini yuboring va biz uni yuklab beramiz.",
            reply_markup=ReplyKeyboardMarkup([[KeyboardButton("📝 Admin Panel")]]) if user.id == ADMIN_ID else None
        )

async def show_admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show admin panel menu"""
    keyboard = [
        [InlineKeyboardButton("⚙️ Bot Sozlamalari", callback_data="admin_settings")],
        [InlineKeyboardButton("📢 Kanallar", callback_data="admin_channels")],
        [InlineKeyboardButton("👥 Foydalanuvchilar", callback_data="admin_users")],
        [InlineKeyboardButton("💬 Vodomark", callback_data="admin_watermark")],
        [InlineKeyboardButton("📊 Statistika", callback_data="admin_stats")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(
        "🛠️ ADMIN PANEL\n\n"
        f"Foydalanuvchi ID: {update.effective_user.id}",
        reply_markup=reply_markup
    ) if update.callback_query else await update.message.reply_text(
        "🛠️ ADMIN PANEL\n\n"
        f"Foydalanuvchi ID: {update.effective_user.id}",
        reply_markup=reply_markup
    )

async def admin_settings_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle admin settings"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("Bot Nomi", callback_data="set_bot_name")],
        [InlineKeyboardButton("Yuklab Olishni Bloklash", callback_data="toggle_block")],
        [InlineKeyboardButton("« Orqaga", callback_data="admin_panel")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    status = "🔴 BLOKLANGAN" if config_manager.config.get("block_downloads") else "🟢 FAOL"
    
    await query.edit_message_text(
        f"⚙️ BOT SOZLAMALARI\n\n"
        f"Bot Nomi: {config_manager.config.get('bot_name', 'VidoGo_Bot')}\n"
        f"Holat: {status}",
        reply_markup=reply_markup
    )

async def admin_channels_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle channel management"""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("➕ Obuna Kanal Qo'shish", callback_data="add_required_channel")],
        [InlineKeyboardButton("📢 Reklama Kanal", callback_data="set_ads_channel")],
        [InlineKeyboardButton("🆘 Qo'llab-Quvvatlash Kanal", callback_data="set_support_channel")],
        [InlineKeyboardButton("« Orqaga", callback_data="admin_panel")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    channels_text = "Majburiy Kanallar:\n"
    for ch in config_manager.config.get("required_channels", []):
        channels_text += f"  • @{ch}\n"
    
    await query.edit_message_text(
        f"📢 KANAL SOZLAMALARI\n\n{channels_text}\n"
        f"Reklama: {config_manager.config.get('ads_channel', 'None')}\n"
        f"Qo'llab-Quvvatlash: {config_manager.config.get('support_channel', 'None')}",
        reply_markup=reply_markup
    )

async def admin_users_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user management"""
    query = update.callback_query
    await query.answer()
    
    stats = config_manager.get_user_stats()
    users_list = "\n".join([
        f"👤 {v['username']} - ID: {k} (Yuklandi: {v.get('downloads', 0)})"
        for k, v in list(config_manager.users.items())[:10]
    ])
    
    keyboard = [
        [InlineKeyboardButton("🔄 Ro'yxatni Yangilash", callback_data="refresh_users")],
        [InlineKeyboardButton("« Orqaga", callback_data="admin_panel")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"👥 FOYDALANUVCHILAR\n\n"
        f"Jami Foydalanuvchilar: {stats['total_users']}\n"
        f"Jami Yukladilgan: {stats['downloads']}\n\n"
        f"Oxirgi 10 Foydalanuvchi:\n{users_list}",
        reply_markup=reply_markup
    )

async def admin_watermark_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle watermark settings"""
    query = update.callback_query
    await query.answer()
    
    current_watermark = config_manager.config.get("watermark_text", "")
    
    keyboard = [
        [InlineKeyboardButton("✏️ Vodomarkni O'zgartirish", callback_data="edit_watermark")],
        [InlineKeyboardButton("« Orqaga", callback_data="admin_panel")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"💬 VODOMARK SOZLAMALARI\n\n"
        f"Joriy Vodomark:\n{current_watermark}",
        reply_markup=reply_markup
    )

async def admin_stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show statistics"""
    query = update.callback_query
    await query.answer()
    
    stats = config_manager.get_user_stats()
    
    keyboard = [
        [InlineKeyboardButton("« Orqaga", callback_data="admin_panel")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"📊 STATISTIKA\n\n"
        f"Jami Foydalanuvchilar: {stats['total_users']}\n"
        f"Jami Yuklangan Videolar: {stats['downloads']}\n"
        f"Saqlash Fayli: {Path('bot_config.json').stat().st_size if Path('bot_config.json').exists() else 0} bytes",
        reply_markup=reply_markup
    )

async def handle_video_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle video download requests"""
    user = update.effective_user
    
    # Check if downloads are blocked
    if config_manager.config.get("block_downloads"):
        await update.message.reply_text("❌ Hozirda yuklash mumkin emas. Admin tomonidan bloklangan.")
        return
    
    # Check subscription
    if not await check_subscription(update, context):
        await update.message.reply_text("🔐 Avval kanalga obuna bo'ling!")
        return
    
    message_text = update.message.text
    
    # Check if it's a URL
    if not (message_text.startswith("http://") or message_text.startswith("https://")):
        await update.message.reply_text("❌ Iltimos, to'g'ri URL yuboring!")
        return
    
    # Send downloading message
    status_msg = await update.message.reply_text("⏳ Video yuklanmoqda...")
    
    try:
        # Download video
        with tempfile.TemporaryDirectory() as tmp_dir:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(tmp_dir, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(message_text, download=True)
                video_file = ydl.prepare_filename(info)
            
            # Send video with watermark
            with open(video_file, 'rb') as f:
                watermark_text = config_manager.config.get("watermark_text", "")
                caption = f"{watermark_text}\n\nⓂ️ {config_manager.config.get('bot_name', 'VidoGo_Bot')}"
                
                await update.message.reply_video(
                    video=f,
                    caption=caption[:1024],  # Telegram caption limit
                    parse_mode="HTML"
                )
            
            # Update user stats
            user_id = str(user.id)
            if user_id in config_manager.users:
                config_manager.users[user_id]["downloads"] = config_manager.users[user_id].get("downloads", 0) + 1
                config_manager.save_users()
            
            await status_msg.delete()
            
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        await status_msg.edit_text(f"❌ Xatolik: {str(e)[:100]}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    if update.effective_user.id != ADMIN_ID and query.data.startswith("admin"):
        await query.answer("❌ Faqat admin!", show_alert=True)
        return
    
    callbacks = {
        "admin_panel": show_admin_menu,
        "admin_settings": admin_settings_handler,
        "admin_channels": admin_channels_handler,
        "admin_users": admin_users_handler,
        "admin_watermark": admin_watermark_handler,
        "admin_stats": admin_stats_handler,
        "check_sub": start,
    }
    
    handler = callbacks.get(query.data)
    if handler:
        await handler(update, context)

async def main():
    """Start the bot"""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_video_download
    ))
    
    # Start bot
    await application.initialize()
    await application.start()
    
    logger.info("Bot ishga tushdi!")
    
    # Keep bot running
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
