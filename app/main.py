import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from config import BOT_TOKEN, WEB_URL1, WEB_URL2

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

"/help yordam komandasi"
    """

    await update.message.reply_text(
        welcome_text,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

# /help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
*Bot Buyruqlari:*

/start - Botni ishga tushirish
/help - Yordam ko'rsatish
/urls - URL'lar ro'yxati

*Tugmalar:*
🌐 Main Site - Asosiy sayt
⚙️ Admin Panel - Admin paneli
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

# /urls komandasi
async def urls_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls_text = f"""
*📋 Bot URL'lari:*

🔸 *Main Site:* `{WEB_URL1}`
🔸 *Admin Panel:* `{WEB_URL2}`

*Tugmalar orqali ochish uchun /start ni bosing.*
    """
    await update.message.reply_text(urls_text, parse_mode='Markdown')

# Boshqa barcha xabarlar
async def all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_text = """
🤖 Men faqat Web App ochish uchun botman.

/start - tugmalarni olish
/help - yordam
/urls - URL'lar ro'yxati
    """
    await update.message.reply_text(response_text)

# Bot ishga tushirish
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlerlar
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("urls", urls_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), all_messages))

    print("🤖 Bot ishga tushdi...")
    print(f"🌐 Main URL: {WEB_URL1}")
    print(f"⚙️ Admin URL: {WEB_URL2}")
    print("\nBotni telegramdan /start bosing!")

    app.run_polling()
