import argparse
from pathlib import Path
import os
import random
from shared_funcs import publish_file_to_telegram, DIRECTORY_IMAGES


def get_random_image():
    if not Path(DIRECTORY_IMAGES).exists():
        print(f"Doesn't exist directory {Path(DIRECTORY_IMAGES).absolute()}")
        return None

    list_of_files = os.listdir(DIRECTORY_IMAGES)

    if len(list_of_files) == 0:
        print(f"{Path(DIRECTORY_IMAGES).absolute()} is empty!")
        return None

    return Path(DIRECTORY_IMAGES, random.choice(list_of_files))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', help='ссылка на фотографию в интернете', type=str)
    parser.add_argument('-f', '--file', help='путь к файлу фотографию локально', type=str)
    args = parser.parse_args()
    link_image = args.link
    file_image = args.file

    if link_image is None and file_image is None:
        file_image = get_random_image()

    if file_image is not None:
        publish_file_to_telegram(file_image)
    elif link_image is not None:
        publish_file_to_telegram(link_image, True)


if __name__ == '__main__':
    main()
