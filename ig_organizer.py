import os
import re
import shutil
from pathlib import Path


postsdir = 'D:/posts/'
mediasdir = Path('D:/midias/delroatacado')

media_regex = re.compile(r'(.+(?=_\d\d-\d)).+(.txt|.mp4|.jpg$)')

for filename in os.listdir(mediasdir):
    media = media_regex.match(filename)

    if media:
        shortcode_dir = Path(os.path.join(
            postsdir, os.path.basename(mediasdir), media.group(1)))

        if shortcode_dir.exists():
            shutil.move(os.path.join(mediasdir, filename), shortcode_dir)
            continue

        os.makedirs(shortcode_dir)
        shutil.move(os.path.join(mediasdir, filename), shortcode_dir)
