# 🎬 VidoGo - Video Yuklab Olish Telegram Boti

Instagram, YouTube, TikTok-dan videolar yuklab olish uchun **Telegram Boti** 🚀

## ✨ Asosiy Features

✅ **Video Yuklab Olish** - Instagram, YouTube, TikTok dan videolar
✅ **Admin Panel** - Barcha sozlamalar bir joyda
✅ **Majburiy Obuna** - Kanalga obuna bo'lishni majburiy qilish
✅ **Vodomark** - Video tagiga custom tekst qo'shish
✅ **Foydalanuvchi Boshqarish** - Barcha foydalanuvchilarni birta joydan ko'rish
✅ **Statistika** - Yuklangan videolar soni, foydalanuvchilar soni

---

## 🔧 Tez Ishga Tushirish

### Lokal Ishga Tushirish:
```bash
# 1. Repository'ni clone qiling
git clone <repo-url>
cd telegram-video-bot

# 2. Virtual environment yarating
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Modullarni o'rnatish
pip install -r requirements.txt

# 4. Bot ishga tushirish
python telegram_video_bot.py
```

### Railway.app-da Deployment:
[SETUP_GUIDE.md](./SETUP_GUIDE.md) faylini o'qing

---

## 📋 Sozlamalar

### Bot Token:
```
7457477557:AAGUBa6qRiI1z67xgESMvWHJwC4bKHBNnCE
```

### Admin ID:
```
8135915671
```

### Bot Nomlar:
- **@VidoGo_Bot** - Asosiy bot
- **@XtraSMMUz** - Additional kanal

---

## 🎯 Admin Panel Commands

| Komanda | Tavsifi |
|---------|---------|
| `/start` | Botni ishga tushirish (Admin panelni ko'rsatish) |
| `⚙️ Bot Sozlamalari` | Bot nomini o'zgartirish, yuklab olishni bloklash |
| `📢 Kanallar` | Obuna, reklama, qo'llab-quvvatlash kanallarini sozlash |
| `👥 Foydalanuvchilar` | Barcha foydalanuvchilarni ko'rish va statistika |
| `💬 Vodomark` | Video tagiga qo'shiladigan teksti o'zgartirish |
| `📊 Statistika` | Bot statistikasini ko'rish |

---

## 📱 Foydalanuvchi Ishlatish

1. **Botni Ishga Tushirish:**
   ```
   /start
   ```

2. **Kanalga Obuna Bo'lish:**
   - Agar obuna bo'lmagansiz, "📺 Kanalga Obuna Bo'ling" tugmasini bosing

3. **Video Yuklash:**
   - Instagram/YouTube/TikTok video linkini yuboring
   - Misol: `https://www.instagram.com/p/ABC123...`

4. **Video Olish:**
   - Bot video yuklaydi va watermark bilan jo'natadi

---

## 🎨 Vodomark Sozlash

Admin Panel → 💬 Vodomark

**Misol:**
```
😀 Ushbu video juda ajoyib uni do'stlaringiz bilan ulashing!

Ⓜ️ @VidoGo_Bot
Ⓜ️ @XtraSMMUz
```

---

## 📊 Fayllar Tuzilishi

```
telegram-video-bot/
├── telegram_video_bot.py      # Asosiy bot kodi
├── requirements.txt           # Python modullar
├── Dockerfile                 # Docker konfiguratsiyasi
├── Procfile                   # Railway deployment
├── railway.json               # Railway sozlamalari
├── SETUP_GUIDE.md            # Deployment qo'llanma
└── README.md                 # Bu fayl
```

---

## 🗄️ Ma'lumot Saqlash

Bot quyidagi fayllarni yaratadi:
- `bot_config.json` - Bot sozlamalari (kanallar, vodomark, ba'lgi)
- `users_data.json` - Foydalanuvchi ma'lumotlari (ID, username, yuklangan soni)

---

## 🔐 Xavfsizlik

- ✅ Faqat admin video sozlamalarini o'zgartira oladi (ID: 8135915671)
- ✅ Foydalanuvchilar majburiy kanalga obuna bo'lishlari kerak
- ✅ Barcha video linklar tekshiriladi
- ✅ Error logging aktiv

---

## 🐛 Debugging

Railway-da logs ko'rish:
```bash
railway logs
```

Lokal testlash:
```python
# Pythonda to'g'ri ishlayotganini tekshiring
python -c "import yt_dlp; print('yt_dlp ishga tushdi')"
```

---

## 📞 Support

Bot xatolig'i bo'lsa:
1. Admin Panel → 🆘 Qo'llab-Quvvatlash Kanal
2. O'zi qayta ishga tushishi uchun kuting (auto-restart)

---

## 📈 O'rganish Uchun

- [python-telegram-bot docs](https://docs.python-telegram-bot.org/)
- [yt-dlp docs](https://github.com/yt-dlp/yt-dlp)
- [Railway docs](https://docs.railway.app/)

---

**Yaratdi:** VidoGo Team
**Versiya:** 1.0
**Last Updated:** 2024

---

## 📝 License

MIT License - Bepul o'rganing va o'zingizning botingizni yarating!

**Foydalanish Shartlari:**
- Qonun-qoidalarga rioya qiling
- Video yuklab olishda mualliflik huquqlari himoyasini o'nglayin
- Commercial foydalanish uchun ruxsatni oling

---

🚀 **Happy Coding!** 🎉
