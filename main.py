import telebot

bot = telebot.TeleBot('7870827647:AAF1dga2RrzpqJFQJslvQ7nUvZq2EmE-0pk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать в мой интернет магазин напишите пожалуйста какой товар вас именно интересует',
                     parse_mode='Markdown')

bot.infinity_polling()