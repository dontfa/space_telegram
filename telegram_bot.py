import telegram

TOKEN = '6074192539:AAGY8zZumfosQEIMoxd9atsr0UOdDMvAUxM'
bot = telegram.Bot(token=TOKEN)

print(bot.get_me())

chat_id = '@cosmosimage2023'
bot.send_message(chat_id=chat_id, text="Hi there again.")