from telebot import TeleBot

rochax_bot = '6388974048:AAHv_YsT-I3lAYiizA0oOg4tq5hsr61XXEM'
bot = TeleBot(rochax_bot)

@bot.message_handler(commands=['start', 'Olá!'])
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o bot da PycodeBR!")

bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()