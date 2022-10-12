from flask import render_template
from config import app


class HomeViews(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        return render_template('home/about.html')

    @staticmethod
    @app.route('/contacts')
    def contacts():
        return render_template('home/contacts.html')

    @staticmethod
    @app.route('/news')
    def news():
        return render_template('home/news.html')
