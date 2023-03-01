import random
import time
import argparse
import telegram
import os
from pathlib import Path

DIRECTORY_ROOT = 'images'


def publish_file_to_telegram(filename):
    TOKEN = '6074192539:AAGY8zZumfosQEIMoxd9atsr0UOdDMvAUxM'
    bot = telegram.Bot(token=TOKEN)
    chat_id = '@cosmosimage2023'

    bot.send_document(chat_id=chat_id, document=open(filename, 'rb'))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sleep', help='период публикации фотографий, секунды', type=int)
    args = parser.parse_args()
    time_sleep = 5 if args.sleep is None else args.sleep

    if not Path(DIRECTORY_ROOT).exists():
        print(f"Doesn't exist directory {Path(DIRECTORY_ROOT).absolute()}")
        return

    list_of_files = os.listdir(DIRECTORY_ROOT)

    while True:
        for x in list_of_files:
            path_to_file = Path(DIRECTORY_ROOT, x)
            publish_file_to_telegram(path_to_file)
            time.sleep(time_sleep)

        random.shuffle(list_of_files)


if __name__ == '__main__':
    main()


