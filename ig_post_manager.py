import os
from pathlib import Path

postsdir = Path('D:/posts')
mediasdir = Path('D:/midias')

first_forn = os.listdir(postsdir)[0]
first_forn_path = Path(os.path.join(postsdir, os.listdir(postsdir)[0]))
first_post = Path(os.path.join(
    first_forn_path, os.listdir(first_forn_path)[0]))
first_post_files = os.listdir(first_post)


def next_post_files():
    stringvar = str()

    for file in first_post_files:
        file_path = Path(os.path.join(first_post, file))

        if file_path.suffix == ".jpg" or file_path.suffix == ".mp4":
            stringvar += f'"{file_path}" '

    return stringvar
