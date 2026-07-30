# 📱 Telegram Video Yuklab Olish Boti - SETUP GUIDE

## 🚀 Railway.app Da Deployment

### 1️⃣ **Railway Akkauntini Yaratish**
- [railway.app](https://railway.app) ga kirish
- GitHub akkauntingiz bilan ro'yxatdan o'tish

### 2️⃣ **Projektni Railway-ga Yuklash**

**Option A: GitHub orqali (Tavsiyalangan)**
```bash
# 1. GitHub-da yangi repository yarating
# 2. Barcha fayllarni push qiling:
git init
git add .
git commit -m "Initial commit"
git push origin main

# 3. Railway.app-da "New Project" → "Deploy from GitHub"
# 4. Repositoryni tanlang
```

**Option B: Railway CLI orqali**
```bash
# Railway CLI o'rnatish
npm install -g @railway/cli

# Railway-ga login qiling
railway login

# Projectni yarating va deploy qiling
railway init
railway up
```

### 3️⃣ **Environment Variables Sozlash**

Railway Dashboard-da quyidagilarni qo'shish:
```
BOT_TOKEN=7457477557:AAGUBa6qRiI1z67xgESMvWHJwC4bKHBNnCE
ADMIN_ID=8135915671
```

### 4️⃣ **Bot Settings Mazka**

Bot ishga tushunaraq quyidagi kanallarni sozlang:

#### **📢 Majburiy Kanallar (Obuna)**
1. Bot bilan `/start` ni bosing
2. Admin Panel → Kanallar
3. "Obuna Kanal Qo'shish" bo'lgan kanallarning ID-larini kiriting

#### **💬 Vodomark Sozlash**
Admin Panel → Vodomark → "✏️ Vodomarkni O'zgartirish"

**Misol:**
```
😀 Ushbu video juda ajoyib uni do'stlaringiz bilan ulashing!

Ⓜ️ @VidoGo_Bot
Ⓜ️ @XtraSMMUz
```

#### **📢 Reklama Kanal**
Admin Panel → Kanallar → "Reklama Kanal"
(Reklama uchun kanal ID-sini kiriting)

#### **🆘 Qo'llab-Quvvatlash Kanal**
Admin Panel → Kanallar → "Qo'llab-Quvvatlash Kanal"
(Qo'llab-quvvatlashtirish uchun kanal ID-sini kiriting)

---

## 🛠️ **Admin Panel Boshlang'ich Qo'llanma**

### Admin Panelga Kirish (Faqat ID: 8135915671)
Telegram-da `/start` yuboring → Admin Panel ko'rinadi

### Admin Menyu:
```
⚙️ Bot Sozlamalari
  ├─ Bot Nomi
  ├─ Yuklab Olishni Bloklash
  
📢 Kanallar
  ├─ Obuna Kanal Qo'shish
  ├─ Reklama Kanal
  └─ Qo'llab-Quvvatlash Kanal
  
👥 Foydalanuvchilar
  ├─ Ro'yxat Yangilash
  ├─ Statistika
  
💬 Vodomark
  ├─ Vodomarkni O'zgartirish
  
📊 Statistika
  ├─ Jami Foydalanuvchilar
  ├─ Jami Yuklangan Videolar
```

---

## 📱 **Foydalanuvchi Features**

### Video Yuklab Olish:
1. Bot bilan `/start` ni bosing
2. Majburiy kanallarga obuna bo'ling
3. Video linkini (Instagram/YouTube/TikTok) yuboring
4. Bot video yuklaydi va watermark bilan jo'natadi

### Qo'llab-Quvvatlashtirish:
Admin Panel → Qo'llab-Quvvatlash Kanal ushun kiriting
Foydalanuvchilar ushbu kanal orqali savollari sora olishadi

---

## 🔧 **Muammolarni Bartaraf Etish**

### ❌ "Video yuklanmaydi"
- FFmpeg o'rnatilganini tekshiring (Railway-da avtomatik)
- URL-ni to'g'ri kiritganingizni tekshiring

### ❌ "Subscription check ishlamaydi"
- Kanal ID-sini to'g'ri kiritganingizni tekshiring
- Formatni tekshiring: `-100` bilan boshlansa, o'zgartiring

### ❌ "Admin Panel ko'rinmaydi"
- Admin ID-sini tekshiring (8135915671)
- Environment variablesni tekshiring

---

## 📊 **Ma'lumotlar Saqlash**

Bot quyidagi fayllarni yaratadi:
- `bot_config.json` - Bot sozlamalari
- `users_data.json` - Foydalanuvchi ma'lumotlari

Railway-da bu fayllar volume ichida saqlanadi.

---

## 🔒 **Xavfsizlik**

✅ Admin-only features
✅ Subscription check
✅ Rate limiting (opsional)
✅ Error logging

---

## 📞 **Support Kanallar Qo'shish**

1. Telegram kanalini yarating (@VidoGo_Bot_Support)
2. Admin Panel → Kanallar → "Qo'llab-Quvvatlash"
3. Kanal ID-sini kiriting

---

## 🚀 **Production Ready**

Bot ishga tayyar! Quyidagilarga e'tibor bering:
- ✅ Token to'g'ri
- ✅ Admin ID to'g'ri
- ✅ Required kanallar sozlangan
- ✅ Vodomark sozlangan

**Server Restart:** Bot avtomatik restartlanadi

---

**Version:** 1.0
**Last Updated:** 2024
