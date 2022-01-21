import imp
import os
import re
import time
import requests
from pathlib import Path
from instabot.Config import HEADERS_GET_REQ_PROFILE

base_dir = Path("D:/midias")


def get_profile_id(response_from_get):
    regex = '"logging_page_id":"profilePage_(\d+)"'

    try:
        user_id = re.search(regex, response_from_get).group(1)
        return user_id

    except AttributeError:
        print('Houve um erro em get_profile_id')
        return None


def get_request_profile(username):
    print('Verificando instagram de: ', username)
    print('==============')
    headers = HEADERS_GET_REQ_PROFILE

    response = requests.get(
        f'https://www.instagram.com/{username}/', headers=headers)

    if response.content == None:
        print("There is no response")
        return None

    return str(response.content)


def media_downloader(midia_format, midias_list):

    for media in midias_list:
        fornecedor = media.fornecedor
        shortcode_dir = Path(os.path.join(base_dir, fornecedor, midia_format, media.shortcode))  # nopep8

        if not shortcode_dir.exists():
            os.makedirs(shortcode_dir)

        for midia in media.midias:
            count = 1
            midia_path = f'{shortcode_dir}/media{midia["extension"]}'

            if os.path.isfile(midia_path):
                midia_path = f'{shortcode_dir}/media_{count}{midia["extension"]}'

            response = requests.get(midia['url'])

            with open(midia_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            count += 1
            print('Baixando nova midia...')
            time.sleep(5)
