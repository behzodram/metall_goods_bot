import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

from config import BOT_TOKEN, WEB_URL1, WEB_URL2

bot = telebot.TeleBot(BOT_TOKEN)

# Start komandasi
@bot.message_handler(commands=['start'])
def start_command(message):
    """Botni ishga tushirish"""
    
    # Tugmalarni yaratish
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    # Birinchi tugma - Main URL
    keyboard.add(
        InlineKeyboardButton(
            "🌐 Main Site",
            web_app=WebAppInfo(url=WEB_URL1)
        )
    )
    
    # Ikkinchi tugma - Admin URL
    keyboard.add(
        InlineKeyboardButton(
            "⚙️ Admin Panel",
            web_app=WebAppInfo(url=WEB_URL2)
        )
    )
    
    # Xabarni yuborish
    welcome_text = """
🤖 *Welcome to Web App Bot!*

🔸 *Main Site* - Asosiy sayt
🔸 *Admin Panel* - Admin paneli

*Tugmalardan birini bosing:*
    """
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

# Help komandasi
@bot.message_handler(commands=['help'])
def help_command(message):
    """Yordam xabari"""
    
    help_text = """
*Bot Buyruqlari:*

/start - Botni ishga tushirish
/help - Yordam ko'rsatish
/urls - URL'lar ro'yxati

*Tugmalar:*
🌐 Main Site - Asosiy sayt
⚙️ Admin Panel - Admin paneli
    """
    
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# URL'lar komandasi
@bot.message_handler(commands=['urls'])
def urls_command(message):
    """URL'lar ro'yxatini ko'rsatish"""
    
    urls_text = f"""
*📋 Bot URL'lari:*

🔸 *Main Site:* `{WEB_URL1}`
🔸 *Admin Panel:* `{WEB_URL2}`

*Tugmalar orqali ochish uchun /start ni bosing.*
    """
    
    bot.send_message(message.chat.id, urls_text, parse_mode='Markdown')

# Barcha boshqa xabarlar
@bot.message_handler(func=lambda message: True)
def all_messages(message):
    """Boshqa barcha xabarlarga javob"""
    
    response_text = """
🤖 Men faqat Web App ochish uchun botman.

/start - tugmalarni olish
/help - yordam
/urls - URL'lar ro'yxati
    """
    
    bot.send_message(message.chat.id, response_text)

# Botni ishga tushirish
if __name__ == '__main__':
    print("🤖 Bot ishga tushdi...")
    print(f"🌐 Main URL: {WEB_URL1}")
    print(f"⚙️ Admin URL: {WEB_URL2}")
    print("\nBotni telegramdan /start bosing!")
    
    bot.polling(none_stop=True)