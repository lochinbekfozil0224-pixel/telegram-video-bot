# 🚀 Railway.app-da Botni Deploy Qilish

## **1-QADAM: GitHub Repositoryni Yaratish**

### 1.1 GitHub-ga kirish
- [github.com](https://github.com) ga kirish
- "New repository" tugmasini bosing

### 1.2 Repository sozlamalari:
```
Repository name: telegram-video-bot
Visibility: Public
Add README: Yes
Add .gitignore: Python
```

### 1.3 Fayllarni Yuklash:
Repository-da "Add file" → "Upload files":

Yuklash kerak bo'lgan fayllar:
```
✓ telegram_video_bot.py
✓ requirements.txt
✓ Dockerfile
✓ Procfile
✓ railway.json
✓ README.md
✓ SETUP_GUIDE.md
```

---

## **2-QADAM: Railway.app-da Akkaunt Yaratish**

### 2.1 Railway-ga kirish
- [railway.app](https://railway.app) ga o'tish
- "Start Free" tugmasini bosing
- GitHub bilan ro'yxatdan o'tish

### 2.2 Email Tekshirish
- Email-ga keladigan tasdiqlash linkini bosing

---

## **3-QADAM: Botni Deploy Qilish**

### 3.1 New Project Yaratish:
1. Dashboard-da "New Project" tugmasini bosing
2. "Deploy from GitHub repo" ni tanlang
3. GitHub-ga o'rnatishni ruxsat bering (authorize)

### 3.2 Repository Tanlash:
- Siz yuklagan `telegram-video-bot` repositoryni tanlang
- "Deploy now" tugmasini bosing

### 3.3 Build va Deploy:
- Railway avtomatik Dockerfile-dan build qiladi
- Deployment 2-5 minut davom etadi
- "Deployed" yozuvi ko'rinsa, tayyor!

---

## **4-QADAM: Environment Variables Sozlash**

### 4.1 Environment Variables-ga kirish:
1. Railway Dashboard-da projectni tanlang
2. "Variables" tab-iga o'tish
3. "New Variable" tugmasini bosing

### 4.2 Quyidagi o'zgaruvchilarni qo'shish:

```
Key: BOT_TOKEN
Value: 7457477557:AAGUBa6qRiI1z67xgESMvWHJwC4bKHBNnCE

Key: ADMIN_ID
Value: 8135915671
```

### 4.3 Saqlash:
"Save" tugmasini bosing

---

## **5-QADAM: Bot Tekshiring**

### 5.1 Telegram-da Bot Test:
```
Telegram-da: @VidoGo_Bot (yoki sizning bot nomingiz)
/start - botni ishga tushiring
```

### 5.2 Admin Panel Ko'rish:
Agar user ID 8135915671 bo'lsa:
- Admin Panel ko'rinadi
- Barcha sozlamalar mavjud

### 5.3 Logs Ko'rish (Debugging):
Railway Dashboard:
1. "Logs" tab-iga o'tish
2. Real-time logs ko'rish

---

## **6-QADAM: Bot Sozlamalarini Qilish**

### 6.1 Admin Panel-da Kirish:
Admin ID-siz `/start` yuboring

### 6.2 Quyidagi sozlamalarni qilish:

**Bot Nomini O'zgartirish:**
- ⚙️ Bot Sozlamalari → Bot Nomi
- Misol: `VidoGo_Bot` yoki `XtraSMMUz_Bot`

**Obuna Kanalini Qo'shish:**
- 📢 Kanallar → ➕ Obuna Kanal Qo'shish
- Kanal ID-sini kiriting
  - Format: `-1001234567890` (minus 100 bilan boshlash kerak!)
  - Yoki: `@channel_username`

**Vodomark Sozlash:**
- 💬 Vodomark → ✏️ Vodomarkni O'zgartirish
- Misol:
```
😀 Ushbu video juda ajoyib uni do'stlaringiz bilan ulashing!

Ⓜ️ @VidoGo_Bot
Ⓜ️ @XtraSMMUz
```

**Reklama Kanal Qo'shish:**
- 📢 Kanallar → 📢 Reklama Kanal
- Reklama joylashtirish uchun kanal ID-si

**Qo'llab-Quvvatlash Kanal:**
- 📢 Kanallar → 🆘 Qo'llab-Quvvatlash Kanal
- Foydalanuvchilar savollari sora olish uchun

---

## **7-QADAM: Kanal ID Topish**

### Telegram Kanal ID'sini Topish:

**Usul 1: Bot ID-ni Yuborish**
```
1. @userinfobot ga message yuboring
2. Bot sizning ID-ingizni ko'rsatadi
3. Kanal ID: -100123456789 (minus bilan boshlaydi)
```

**Usul 2: Username orqali**
```
Agar kanal username-i @mychannel bo'lsa:
- Channelga @userinfobot admin qilib qo'ying
- Bot kanal ID-ni ko'rsatadi
```

**Usul 3: Desktop/Web**
```
Channel linki: t.me/c/123456789
Kanal ID: -100123456789 (minus 100 + raqamlar)
```

---

## **8-QADAM: Bot Ishga Tayyorligini Tekshirish**

### Checklist:
- [ ] Railway-da Deploy qilindi
- [ ] Environment Variables sozlandi
- [ ] Bot Telegram-da ishga tushdi
- [ ] Admin Panel ko'rini
- [ ] Obuna kanallar qo'shildi
- [ ] Vodomark sozlandi
- [ ] Video yuklab olish test qilindi

---

## **🔄 Bot Restart Qilish**

Railway-da bot avtomatik restartlanadi, lekin kerak bo'lsa:

1. Railway Dashboard-da Project tanlang
2. "Settings" → "Danger" bo'limi
3. "Redeploy" yoki "Restart" tugmasini bosing

---

## **⚠️ Muammolarni Bartaraf Etish**

### ❌ Bot ishlamaydi
```
1. Logs ko'ring (Railway → Logs)
2. Token to'g'ri yozilganini tekshiring
3. Restart qiling (Railway → Redeploy)
```

### ❌ Video yuklanmaydi
```
1. FFmpeg o'rnatilganini tekshiring (Dockerfile-da bor)
2. URL to'g'ri yo'li kiritilganini tekshiring
3. Bot logs-da xatoni ko'ring
```

### ❌ Admin Panel ko'rinmaydi
```
1. Admin ID tekshiring (8135915671)
2. Environment Variables tekshiring
3. Bot restart qiling
```

### ❌ Kanal subscription ishlamaydi
```
1. Kanal ID formatini tekshiring (-100... bilan boshlaydi)
2. Botni admin qilip qo'ying kanalda
3. ID tekshirish uchun @userinfobot'dan foydalaning
```

---

## **💾 Ma'lumot Saqlash**

Railway-da fayllar jo'xqali bo'ladi (ephemeral). 
**Doimiy saqlash uchun:**

1. Railway Dashboard → "Data" tab
2. PostgreSQL yoki MongoDB qo'shing
3. Bot kodi-da ma'lumotlarni database-ga saqlang

---

## **📊 Monitoring**

### Railway-da Monitoring:
1. "Deployments" tab - Deploy tarixi
2. "Logs" tab - Real-time logs
3. "Metrics" tab - CPU, Memory, Network

### Avtomatik Restart:
- Railway bot xato bo'lsa avtomatik restartlanadi
- Log-larda xatoni ko'rish mumkin

---

## **🎉 TAYYOR!**

Bot ishga tushdi! Quyidagilarn barcha qilganingizni tekshiring:

✅ Bot Telegram-da javob beradi
✅ `/start` komandasi ishlaydi
✅ Admin Panel mavjud (Admin ID uchun)
✅ Kanallar sozlangan
✅ Video yuklab olish ishlaydi
✅ Watermark qo'shilib boradiยา

---

**Batafsil Qo'llanma:** [SETUP_GUIDE.md](./SETUP_GUIDE.md)

**Support:** Railway docs - [docs.railway.app](https://docs.railway.app/)

---

🚀 **Happy Deploying!** 🎉
