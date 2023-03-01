import random
import time
import argparse
import os
from pathlib import Path
from shared_funcs import publish_file_to_telegram, DIRECTORY_IMAGES


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sleep', help='период публикации фотографий, секунды', type=int)
    args = parser.parse_args()
    time_sleep = 14400 if args.sleep is None else args.sleep

    if not Path(DIRECTORY_IMAGES).exists():
        print(f"Doesn't exist directory {Path(DIRECTORY_IMAGES).absolute()}")
        return

    list_of_files = os.listdir(DIRECTORY_IMAGES)

    while True:
        for x in list_of_files:
            path_to_file = Path(DIRECTORY_IMAGES, x)
            publish_file_to_telegram(path_to_file)
            time.sleep(time_sleep)

        random.shuffle(list_of_files)


if __name__ == '__main__':
    main()


