from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '6281796769:AAHQEx0eth_mHj257nfrCUQM_YofsOWWGG0'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = f'Hi👋!\t{message.from_user.full_name} Welcome Cyrillic_Latin Transliterator'
    answer += '\n Enter your text'
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))


bot.polling()
