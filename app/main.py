import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from config import BOT_TOKEN, BOT_USERNAME, WEB_URL1, WEB_URL2

# Commands fayldan import qilamiz
from commands import stats, help_command, share

# Logger
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start komandasi
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 Main Site", web_app=WebAppInfo(url=WEB_URL1))],
        [InlineKeyboardButton("⚙️ Admin Panel", web_app=WebAppInfo(url=WEB_URL2))]
    ])

    welcome_text = """
🤖 *Welcome to Web App Bot!*

🔸 *Main Site* - Asosiy sayt
🔸 *Admin Panel* - Admin paneli

*Tugmalardan birini bosing:*

/help yordam komandasi
    """

    await update.message.reply_text(
        welcome_text,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

# Boshqa barcha xabarlar
async def all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_text = """
🤖 Men faqat Web App ochish uchun botman.

/start - tugmalarni olish
/help - yordam
    """
    await update.message.reply_text(response_text)

# Bot ishga tushirish
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlerlar
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", help_command))
    # share uchun lambda orqali BOT_USERNAME beriladi
    app.add_handler(CommandHandler("share", lambda u, c: share(u, c, BOT_USERNAME)))

    # Web handler
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), all_messages))

    print("🤖 Bot ishga tushdi...")
    print(f"🌐 Main URL: {WEB_URL1}")
    print(f"⚙️ Admin URL: {WEB_URL2}")
    print("\nBotni telegramdan /start bosing!")

    app.run_polling()
