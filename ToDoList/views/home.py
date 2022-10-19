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

    @app.errorhandler(404)
    def not_found(e):
        return render_template("home/404.html", context={})