import requests
import argparse
from pathlib import Path
from datetime import datetime
from shared_funcs import download_picture, DIRECTORY_IMAGES, NASA_API_KEY


def main():
    path_dir = DIRECTORY_IMAGES
    if not Path(path_dir).exists():
        Path(path_dir).mkdir(parents=True, exist_ok=False)

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='количество фотографий', type=int)
    args = parser.parse_args()
    count = 1 if args.count is None else args.count

    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_API_KEY}'
    response = requests.get(url)

    list_response = response.json()
    for i, x in enumerate(list_response):
        filename = x['image']
        date_file = x['date']
        obj_date = datetime.fromisoformat(date_file).date()
        url_file = f'https://api.nasa.gov/EPIC/archive/natural/{obj_date.year}/{obj_date.month:02}' \
                   f'/{obj_date.day}/png/{filename}.png?api_key={NASA_API_KEY}'

        path_to_file = Path(path_dir, f'nasa_epic_{i}.png')
        download_picture(url_file, path_to_file)
        if i >= count-1:
            break


    print(f'Загрузка завершена. Количество загруженных фото: {i + 1}')


if __name__ == '__main__':
    main()
