import time
import instaloader
from db_main import Post
from datetime import datetime
from itertools import takewhile


L = instaloader.Instaloader(dirname_pattern='/midias/{target}',
                            save_metadata=False,
                            filename_pattern='{date_utc:%Y-%m-%d_%H-%M-%S}_{shortcode}',
                            post_metadata_txt_pattern='{likes} likes - {comments} comments. \n {caption} ')

L.load_session_from_file(
    'segredosdaslojas', 'D:\Programming\Projetos\instagramBotComments\session-segredosdaslojas')

targets = ["natural_paglaplus", "sairet_confeccoes", 'pamelita_modas_oficial',
           'lekadrye', 'bacarinismodas', 'luepeixoto_fashion',
           'delroatacado', 'popmodaslegg', 'fabismarmodas', 'modas_yurian',
           'pop.modasjeans', 'modas_lindo']


def downloader():

    for target in targets:
        profile = instaloader.Profile.from_username(L.context, target)
        posts = instaloader.Profile.get_posts(profile)

        print('Verificando novidades em : ', target)

        for post in takewhile(lambda p: p.date_local > datetime(2022, 1, 9), posts):
            shortcode = post.__dict__['_node']['shortcode']

            post_seen = Post.find_shortcode(shortcode)
            if post_seen:
                print(shortcode + ' ja estava registrado')
                break

            print(shortcode, " Sera adicionado ao DB")
            Post.add(target, shortcode)
            L.download_post(post, target)

            print('Timer entre downloads.... 2min')
            time.sleep(120)

        print('Timer entre fornecedores... 3min')
        print('================================')
        print('================================')
        time.sleep(180)
