import json
import os
from telegram import Update
from telegram.ext import ContextTypes

# Foydalanuvchilarni saqlash fayli
USERS_FILE = "users.json"

# Foydalanuvchilar setini yuklash yoki bo'sh yaratish
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users = set(json.load(f))
else:
    users = set()

# stats komandasi
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bot foydalanuvchilari soni: {len(users)}")

# help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Bot quyidagi buyruqlarni qo‘llab-quvvatlaydi:\n\n"
        "/start - Botni ishga tushirish va matn ajratish uchun tayyorlash\n"
        "/stats - Bot foydalanuvchilari sonini ko‘rish\n"
        "/share - Bot username’ini nusxa olish\n"
        "/help - Bu yordam oynasini ko‘rish"
    )
    await update.message.reply_text(help_text)

# share komandasi
async def share(update: Update, context: ContextTypes.DEFAULT_TYPE, BOT_USERNAME: str):
    await update.message.reply_text(
        f"Bot username-si:\n{BOT_USERNAME}\n\n"
        "Username’ni nusxa olish uchun shu matnni tanlab copy qiling."
    )
