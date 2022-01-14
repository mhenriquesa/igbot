import json
import requests
from Config import HEADERS, POPMODASJEANS, LEKADRYE, PAGLAPLUS, DELROA


def stories_checker(fornecedor):
    target = fornecedor
    headers = HEADERS

    response = requests.get(
        f'https://i.instagram.com/api/v1/feed/user/{target}/story/', headers=headers)
    print(response.content)

    data = json.loads(response.content)

    stories = data['reel']['items']
    fornecedor = data['reel']['user']['username']
    print('===================')
    print('Fornecedor: ', fornecedor)
    print('===================')

    for story in stories:
        cod = story['code']
        print('story code: ', cod)

        if 'video_duration' in story:
            videoduration = story['video_duration']
            video_link = story['video_versions'][0]['url']
            print('----')
            print('Story is a video')
            print('  ')
            print('Video duration: ', videoduration)
            print('Video link: ', video_link)
            print('----')
            continue

        imgurl = story['image_versions2']['candidates'][0]['url']

        print('Story is a image')
        print('----')
        print('Link da foto ', imgurl)

        print('----------------')


def stories_downloader():
    file_url = ''
    response = requests.get(file_url, stream=True)

    with open('story.jpg', "wb") as jpg:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                jpg.write(chunk)


# stories_downloader()
stories_checker(DELROA)
