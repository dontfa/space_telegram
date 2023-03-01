import requests
from urllib.parse import urlsplit, unquote
import os


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

