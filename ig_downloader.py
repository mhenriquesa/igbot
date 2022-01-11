import time
from instaloader_downloads import downloader
from ig_organizer import organizer

try:
    while True:
        try:
            downloader()
        except:
            print('deu erro ou user desligou o loop')

        print('Loop concluido...ou user cancelou o Loop')
        print('Aguardando 10min proximo loop')
        time.sleep(600)


except KeyboardInterrupt:
    pass

try:
    print('Organizando midias... Separando por posts...')
    organizer()

except:
    print(' Erro ao organizar midias')

print('Done')
