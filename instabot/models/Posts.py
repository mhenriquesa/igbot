import re
import json
import requests
from instabot import db
from instabot.Config import QUERY_HASH, HEADERS_GET_REQ_PROFILE, HEADERS_DOWNLOAD_FIRST_12_POSTS


class Posts(db.Model):
    __tablename__ = 'posts'

    Rowid = db.Column(db.Integer(), primary_key=True)
    fornecedor = db.Column(db.String(20), nullable=False)
    shortcode = db.Column(db.String(10), nullable=False, unique=True)

    def __init__(self, fornecedor, shortcode):
        self.fornecedor = fornecedor
        self.shortcode = shortcode
        self.has_children = False
        self.midias = []

    def __repr__(self):
        return f"Post < fornecedor: {self.fornecedor}, shortcode: {self.shortcode} , Has children: {self.has_children} , Midias: {self.midias} >"

    def to_json(self):
        return {
            "fornecedor": self.fornecedor,
            "shortcode": self.shortcode,
            "has_children": self.has_children,
            "midias": self.midias
        }

    @classmethod
    def find_shortcode_in_db(cls, shortcode):
        return db.session.query(Posts).filter(Posts.shortcode == shortcode).first()

    @classmethod
    def add_shortcode_in_db(cls, fornecedor, shortcode):
        shortcodetoadd = Posts(fornecedor, shortcode)

        db.session.add(shortcodetoadd)
        db.session.commit()

    @classmethod
    def get_request_profile(cls, username):
        print('Verificando feed de: ', username)
        print('==============')
        headers = HEADERS_GET_REQ_PROFILE

        response = requests.get(
            f'https://www.instagram.com/{username}/', headers=headers)

        if response.content == None:
            print("There is no response")
            return None

        return str(response.content)

    @classmethod
    def get_first_12_posts(cls, profile_id, end_cursor):
        headers = HEADERS_DOWNLOAD_FIRST_12_POSTS
        example = {"id": "", "first": 12, "before": "QQ=="}

        example['id'] = profile_id
        example['before'] = end_cursor
        variables = json.dumps(example)

        params = (
            ('query_hash', QUERY_HASH),
            ('variables', variables),
        )

        response = requests.get(
            'https://www.instagram.com/graphql/query/', headers=headers, params=params)

        r = response.json()
        return r

    @classmethod
    def get_end_cursor(cls, response_from_get):
        regex1 = '"edge_owner_to_timeline_media":{"count":\d+,"page_info":{"has_next_page":.+,"end_cursor":"(.{115,126})(?="})'

        try:
            end_cursor = re.search(regex1, response_from_get).group(1)
            return end_cursor

        except AttributeError:
            print("aconteceu um erro em 'get_end_cursor'")
            return None

    @classmethod
    def get_profile_id(cls, response_from_get):
        regex2 = '"logging_page_id":"profilePage_(\d+)"'

        try:
            user_id = re.search(regex2, response_from_get).group(1)
            return user_id

        except AttributeError:
            print('Houve um erro em get_profile_id')
            return None

    @classmethod
    def get_posts_links_from_json(cls, json):
        posts_list = json['data']['user']['edge_owner_to_timeline_media']['edges']
        posts_informations_list = list()

        db_insert_controller = False  # Somente o primeiro post vai ser colocado no DB

        for post in posts_list:
            shortcode = post['node']['shortcode']

            if cls.find_shortcode_in_db(shortcode):
                break

            owner = post['node']['owner']['username']
            p = Posts(owner, shortcode)

            if 'edge_sidecar_to_children' in post['node']:
                p.has_children = True
                children_nodes = post['node']['edge_sidecar_to_children']['edges']

                for child_node in children_nodes:
                    is_video = child_node['node']['is_video']

                    if is_video:
                        url = child_node['node']['video_url']
                        extension = ".mp4"
                    else:
                        url = child_node['node']['display_url']
                        extension = ".jpg"

                    p.midias.append({"url": url, "extension": extension})

            else:
                is_video = post['node']['is_video']
                if is_video:
                    url = post['node']['video_url']
                    extension = ".mp4"
                else:
                    url = post['node']['display_url']
                    extension = ".jpg"

                p.midias.append({"url": url, "extension": extension})

            posts_informations_list.append(p)

            if db_insert_controller == False:
                Posts.add_shortcode_in_db(owner, shortcode)
                db_insert_controller = True

        return posts_informations_list
