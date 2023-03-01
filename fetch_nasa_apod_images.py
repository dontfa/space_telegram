import requests
import argparse
from pathlib import Path
from shared_funcs import download_picture, get_file_extension


def main():
    path_dir = 'images'
    if not Path(path_dir).exists():
        Path(path_dir).mkdir(parents=True, exist_ok=False)

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='количество фотографий', type=int)
    args = parser.parse_args()
    count = 1 if args.count is None else args.count


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

    print(f'Загрузка завершена. Количество загруженных фото: {i + 1}')


if __name__ == '__main__':
    main()
