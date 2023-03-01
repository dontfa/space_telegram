import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
from datetime import datetime


def get_links_spaceX(url):
    response = requests.get(url)
    response.raise_for_status()

    dict_resp = response.json()
    return dict_resp['links']['flickr']['original']


def fetch_spacex_last_launch(path_dir):
    links_picture = get_links_spaceX('https://api.spacexdata.com/v5/launches/latest/')
    if len(links_picture) == 0:
        links_picture = get_links_spaceX('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')

    for i, x in enumerate(links_picture):
        path_to_file = Path(path_dir, f'spacex{i}.jpg')
        download_picture(x, path_to_file)


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


def fetch_nasa_pictures(path_dir, count=1):
    api_key = 'GxRngRl9Lqka1duiCcFgCzneA578KcVB8NvoFjKu'
    url = f'https://api.nasa.gov/planetary/apod'
    payloads = {
        'api_key': api_key,
        'count': count,
    }

    response = requests.get(url, params=payloads)
    links_picture = []
    for x in response.json():
        links_picture.append(x['hdurl'])

    for i, x in enumerate(links_picture):
        path_to_file = Path(path_dir, f'nasa_apod_{i}{get_file_extension(x)}')
        download_picture(x, path_to_file)


def fetch_nasa_epic_pictures(path_dir):
    api_key = 'GxRngRl9Lqka1duiCcFgCzneA578KcVB8NvoFjKu'
    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}'

    response = requests.get(url)
    response.raise_for_status()

    list_response = response.json()
    for i, x in enumerate(list_response):
        filename = x['image']
        date_file = x['date']  #"2023-02-27 00:50:27"
        obj_date = datetime.fromisoformat(date_file).date()
        url_file = f'https://api.nasa.gov/EPIC/archive/natural/{obj_date.year}/{obj_date.month:02}' \
                   f'/{obj_date.day}/png/{filename}.png?api_key={api_key}'

        print(url_file)

        path_to_file = Path(path_dir, f'nasa_epic_{i}.png')
        download_picture(url_file, path_to_file)
        if i > 1:
            break


def main():
    path_dir = 'images'

    if not Path(path_dir).exists():
        Path(path_dir).mkdir(parents=True, exist_ok=False)

    #fetch_spacex_last_launch(path_dir)
    #fetch_nasa_pictures(path_dir, 5)
    fetch_nasa_epic_pictures(path_dir)


if __name__ == '__main__':
    main()
