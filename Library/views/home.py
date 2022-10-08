from flask import render_template
from config import app


class HomeViews(object):

    @staticmethod
    @app.route('/')
    def home_index():
        return render_template('home/index.html', context={})

    @staticmethod
    @app.route('/home/about')
    def home_about():
        return render_template('home/about.html', context={})

    @staticmethod
    @app.route('/home/contact')
    def home_contact():
        return render_template('home/contact.html', context={})

    @staticmethod
    @app.route('/home/feedback')
    def home_feedback():
        return render_template('home/feedback.html', context={})

    @app.errorhandler(404)
    def not_found(e):
        return render_template("home/404.html", context={})
