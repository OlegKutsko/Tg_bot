import telebot
import functions
import config

#Token from @BotFather
bot = telebot.TeleBot(config.TOKEN)


# Handling the /start function
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Отправляйте Ваш csv файл)')


#Handle csv file
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:\\Users\\User\\PycharmProjects\\pythonProject\\Tg_bot\\Received\\ ' + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, func.processing_csv_file(message.document.file_name))
    func.grafic(message.document.file_name)
    graphic = open('graphic.png', 'rb')
    bot.send_photo(message.chat.id, graphic)

bot.polling(none_stop=True, interval=0)
