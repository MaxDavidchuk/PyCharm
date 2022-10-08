from flask import render_template, request, session, redirect, make_response
from config import app


class BookViews(object):

    @staticmethod
    @app.route('/book/main', methods=['GET', 'POST'])
    def book_main():
        """ Перегляд усіх книжок """
        if request.method == 'GET':
            return render_template('book/main.html', context={})
        elif request.method == 'POST':
            return render_template('book/main.html', context={})
