import os
import re
import shutil
from pathlib import Path


postsdir = Path('D:/posts')
mediasdir = Path('D:/midias')
fornecedores = os.listdir(mediasdir)

media_regex = re.compile(
    r'([0-9-_]{20}([a-zA-Z0-9-_]{11}))_?\d?\d?(.jpg|.mp4|.txt)')


def organizer():
    for fornecedor in fornecedores:
        fornecedor_dir = Path(os.path.join(mediasdir, fornecedor))
        midias = os.listdir(fornecedor_dir)
        print(fornecedor)

        for midia in midias:
            midia_match = media_regex.match(midia)
            print(midia_match)

            shortcode_post_dir = Path(os.path.join(
                postsdir, fornecedor, midia_match.group(1)))

            if shortcode_post_dir.exists():
                shutil.move(os.path.join(mediasdir, fornecedor, midia),
                            shortcode_post_dir)
                continue

            os.makedirs(shortcode_post_dir)
            shutil.move(os.path.join(mediasdir, fornecedor, midia),
                        shortcode_post_dir)

        if not any(os.scandir(fornecedor_dir)):
            Path.rmdir(fornecedor_dir)


def backfiles(fornecedor):
    fornecedor_dir = os.path.join(postsdir, fornecedor)

    for path, y, files in os.walk(fornecedor_dir):
        parent_dir = os.path.basename(os.path.dirname(path))

        for f in files:
            file = os.path.join(path, f)
            shutil.move(file, os.path.join(mediasdir, parent_dir))


organizer()
