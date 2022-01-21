import time
from instabot import util
from instabot.Config import TARGETS
from instabot.models.Posts import Posts


def download_posts():
    for target in TARGETS:

        response = Posts.get_request_profile(target)
        user_id = Posts.get_profile_id(response)
        end_cursor = Posts.get_end_cursor(response)
        posts_json = Posts.get_first_12_posts(user_id, end_cursor)
        posts_informations_list = Posts.get_posts_links_from_json(posts_json)

        if posts_informations_list == []:
            print('Nenhuma atualizacao no fornecedor: ', target)
            print('Chamando proximo fornecedor')
            print('Time entre fornecedores... 10s')
            time.sleep(10)
            continue

        util.media_downloader("post", posts_informations_list)
        print('Time entre fornecedores... 10s')
        time.sleep(10)
