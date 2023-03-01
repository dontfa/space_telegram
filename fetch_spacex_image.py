import requests
import argparse
from pathlib import Path
from shared_funcs import download_picture


def get_links_spacex(url):
    response = requests.get(url)
    response.raise_for_status()

    dict_resp = response.json()
    return dict_resp['links']['flickr']['original']


def main():
    path_dir = 'images'
    if not Path(path_dir).exists():
        Path(path_dir).mkdir(parents=True, exist_ok=False)

    parser = argparse.ArgumentParser()
    parser.add_argument('-id', help='идентификатор фотографий')
    args = parser.parse_args()
    id_photos = args.id

    if id_photos is None:
        links_picture = get_links_spacex('https://api.spacexdata.com/v5/launches/latest/')
    else:
        links_picture = get_links_spacex(f'https://api.spacexdata.com/v5/launches/{id_photos}')

    if len(links_picture) == 0:
        print('Список полученных фотографий пуст. (', 'latest' if id_photos is None else f'by id {id_photos}', ')')
        return

    for i, x in enumerate(links_picture):
        path_to_file = Path(path_dir, f'spacex{i}.jpg')
        download_picture(x, path_to_file)

    print(f'Загрузка завершена. Количество загруженных фото: {i+1}')


if __name__ == '__main__':
    main()
