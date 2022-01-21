import os
import time
import json
import requests
from instabot import db
from pathlib import Path
from instabot.Config import HEADERS_STORIES_REQUEST_DATA_RAW


class Stories(db.Model):
    __tablename__ = 'stories'

    Rowid = db.Column(db.Integer(), primary_key=True)
    fornecedor = db.Column(db.String(20), nullable=False)
    shortcode = db.Column(db.String(10), nullable=False, unique=True)

    stories_dir = Path("midias/stories")

    def __init__(self, fornecedor, code=None, link=None, type=None):
        self.fornecedor = fornecedor
        self.shortcode = code
        self.midias = []

    def to_json(self):
        return {
            "fornecedor": self.fornecedor,
            "code": self.code,
            "link": self.link,
            "type": self.type
        }

    @classmethod
    def find_shortcode_in_db(cls, shortcode):
        return db.session.query(Stories).filter(Stories.shortcode == shortcode).first()

    @classmethod
    def insert_shortcode_in_db(cls, fornecedor, shortcode):

        shortcodetoadd = Stories(fornecedor, shortcode)

        db.session.add(shortcodetoadd)
        db.session.commit()

    @classmethod
    def request_data_raw(cls, fornecedor_id, fornecedor_username):
        headers = HEADERS_STORIES_REQUEST_DATA_RAW

        response = requests.get(
            f'https://i.instagram.com/api/v1/feed/user/{fornecedor_id}/story/', headers=headers)

        data_raw = json.loads(response.content)

        if data_raw['reel'] == None:
            return None

        return {
            "fornecedor": fornecedor_username,
            "stories": data_raw['reel']['items']
        }

    @classmethod
    def get_stories_informations(cls, stories_raw, fornecedor_username):
        if stories_raw == None:
            print("Nenhum story disponivel no momento")
            return None

        stories_list = stories_raw['stories']
        fornecedor = fornecedor_username
        db_inserted_controller = False

        stories = list()

        for story in stories_list:
            if Stories.find_shortcode_in_db(story['code']):
                print('Story ja baixado... Passando pro proximo fornecedor')
                break

            st = Stories(fornecedor)
            st.shortcode = story['code']

            if 'video_duration' in story:
                midia = {"url": story['video_versions']
                         [0]['url'], "extension": ".mp4"}

                st.midias.append(midia)
                stories.append(st)
                continue

            midia = {"url": story['image_versions2']
                     ['candidates'][0]['url'], "extension": ".jpg"}
            st.midias.append(midia)

            stories.append(st)

            if db_inserted_controller == False:
                Stories.insert_shortcode_in_db(fornecedor, story['code'])
                db_inserted_controller = True

        return stories

    @classmethod
    def rendered(cls, stories_raw):

        for story in stories_raw:
            print('Fornecedor: ', story.fornecedor)
            print('shortcode : ', story.shortcode)
            print('midias: ', story.midias)
            print('========')
