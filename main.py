
import telebot
import webbrowser

bot = telebot.TeleBot('6295179051:AAHGTmW9WdvO850ymdsGEEgtc88I71m93zI')
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://pribalt.info/hokkei/vhl/tablica')
@bot.message_handler(commands=['team'])
def site(message):
    webbrowser.open('https://cska-hockey.ru/')
@bot.message_handler(commands=['trainer'])
def site(message):
    webbrowser.open('https://ru.wikipedia.org/wiki/%D0%A4%D1%91%D0%B4%D0%BE%D1%80%D0%BE%D0%B2,_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9_%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%87')
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, хочешь узнать больше о хоккее? ')
@bot.message_handler()
def info(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Тогда введи запрос, которой тебе больше всего интересен: турнирная таблица, лучшая хоккейная команда, лучший тренер хоккея')
    elif message.text.lower() == 'турнирная таблица':
        bot.reply_to(message, 'можешь перейти на сайт, для этого введи команду /site')
    elif message.text.lower() == 'лучшая хоккейная команда':
        bot.reply_to(message, 'ЦСКА, чтобы перейти на их сайт введи команду /team')
    elif message.text.lower() == 'лучший тренер хоккея':
        bot.send_message(message.chat.id,'Сергей Фёдоров, если хочешь узнать больше о его биографии введи команду /trainer')
    else:
        bot.send_message(message.chat.id,'к сожалению этот бот не может вам помочь')




bot.polling(none_stop=True)