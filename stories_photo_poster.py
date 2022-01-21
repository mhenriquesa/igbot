# Working OK

import os
import random
import string
import requests
from instabot.Config import DATA_PHOTO_STORY_POSTER, HEADERS_STORY_PHOTO_POSTER, HEADERS_STORY_PHOTO_UPLOADER, MIDIA_UPLOADER_PROFILE_ID, PARAM_STORY_PHOTO_UPLOADER


def midia_uploader(photo_path):
    headers = HEADERS_STORY_PHOTO_UPLOADER
    params = PARAM_STORY_PHOTO_UPLOADER

    data = {
        'source': 8,
        'profile_id': MIDIA_UPLOADER_PROFILE_ID,
        'waterfallxapp': "web_react_composer",
        'upload_id': random.randint(1020, 1040)
    }

    filename = photo_path
    files = {'farr': (os.path.basename(filename), open(
        filename, 'rb'), 'application/octet-stream')}

    response = requests.post('https://upload-business.facebook.com/ajax/react_composer/attachments/photo/upload',
                             headers=headers, params=params, data=data, files=files)

    print(response.content)
    print(response.status_code)


def id_generator(size=5, chars=string.digits):

    composer_session_id = "a7418c51-3d95-478c-9fca-"
    return composer_session_id + ''.join(random.choice(chars) for _ in range(size))


def story_poster():

    headers = HEADERS_STORY_PHOTO_POSTER
    data = DATA_PHOTO_STORY_POSTER

    response = requests.post(
        'https://business.facebook.com/api/graphql/', headers=headers, data=data)

    print(response.content)
    print(response.status_code)


story_poster()
