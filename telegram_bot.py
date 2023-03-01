import telegram

TOKEN = '6074192539:AAGY8zZumfosQEIMoxd9atsr0UOdDMvAUxM'
bot = telegram.Bot(token=TOKEN)

print(bot.get_me())

chat_id = '@cosmosimage2023'
#bot.send_message(chat_id=chat_id, text="Hi there again.")

#bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_0.jpg', 'rb'))

#bot.send_document(chat_id=chat_id, document='https://python-telegram-bot.org/static/testfiles/telegram.gif'))
bot.send_document(chat_id=chat_id, document='https://apod.nasa.gov/apod/image/9707/mars1_pathfinder_big.jpg')