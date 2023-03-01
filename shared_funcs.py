import requests
import telegram
import os
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv
load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")
TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
DIRECTORY_IMAGES = os.getenv("SPACE_TELEGRAM_DIRECTORY_IMAGES")
NASA_API_KEY = os.getenv("NASA_API_KEY")


def download_picture(url, filename):

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):

    split_url = urlsplit(url)
    unq_path = unquote(split_url.path)

    _, filename = os.path.split(unq_path)
    _, extension = os.path.splitext(filename)

    return extension


def publish_file_to_telegram(filename, flag_link=False):
    bot = telegram.Bot(token=TOKEN_TELEGRAM)

    if flag_link:
        document_for_publish = filename
    else:
        document_for_publish = open(filename, 'rb')

    bot.send_document(chat_id=CHAT_ID, document=document_for_publish)


