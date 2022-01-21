from instabot import db
from instabot.controllers import posts_controller
from instabot.controllers import stories_controller
from flask import render_template, Blueprint, url_for, Response
main = Blueprint('main', __name__)

posts = [
    {
        'fornecedor': 'Fabismar',
        'video': 'Fabismar foto bonita'
    },
    {
        'fornecedor': 'Pop',
        'video': 'Jeans'
    }
]


@main.route('/')
@main.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/download_stories',  methods=['POST'])
def post_download_stories():
    stories_controller.download_stories()

    print('Recebido!')
    return Response(status=200)


@main.route('/download_posts',  methods=['POST'])
def post_download_posts():
    posts_controller.download_posts()

    return Response(status=200)
