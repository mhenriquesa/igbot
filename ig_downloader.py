import time
from datetime import datetime
from itertools import takewhile
import instaloader

L = instaloader.Instaloader(save_metadata=False)

L.load_session_from_file(
    'segredosdaslojas', 'D:\Programming\Projetos\instagramBotComments\session-segredosdaslojas')

targets = ["sairet_confeccoes", 'pamelita_modas_oficial', 'lekadrye', 'bacarinismodas', 'luepeixoto_fashion',
           'delroatacado', 'popmodaslegg', 'fabismarmodas', 'modas_yurian', 'pop.modasjeans', 'modas_lindo']

try:
    while True:
        try:
            for target in targets:
                print('Olhando: ' + target)
                profile = instaloader.Profile.from_username(L.context, target)
                posts = instaloader.Profile.get_posts(profile)

                for post in takewhile(lambda p: p.date_local > datetime(2022, 1, 5), posts):
                    r = L.download_post(post, target)
                    if r == False:
                        break
                print('Time entre fornecedores.... 6min ')
                time.sleep(360)
        except:
            print('deu erro ou user desligou o loop')
        print('Loop concluido...')
        time.sleep(5)

except KeyboardInterrupt:
    pass
