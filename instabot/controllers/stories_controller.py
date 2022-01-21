from instabot import util
from instabot.Config import TARGETS
from instabot.models.Stories import Stories


def download_stories():
    for fornecedor in TARGETS:
        response = util.get_request_profile(fornecedor)
        user_id = util.get_profile_id(response)
        data_raw_items = Stories.request_data_raw(user_id, fornecedor)
        stories_info = Stories.get_stories_informations(data_raw_items, fornecedor)  # nopep8

        if stories_info == None:
            print('Nenhum story disponivel em: ', fornecedor)
            print('Chamando proximo fornecedor...')
            continue

        # Stories.rendered(stories_info)
        util.media_downloader("story", stories_info)
        break
