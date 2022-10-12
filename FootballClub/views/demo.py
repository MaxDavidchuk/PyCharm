from flask import render_template, session
from config import app, mongo
from time import strftime
from hashlib import md5


class DemoViews(object):

    @staticmethod
    @app.route('/create_user')
    def create_user():
        mongo.db.users.insert_one({
            'login': 'admin123',
            'pwd': '928685e214fa387530cc8e14d09a1858',
            'email': 'admin123@ukr.net',
            'reg_date': strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'Super-Admin'
        })
        return render_template('demo/create_user.html', context={
            'msg': 'Користувач [admin123] - успішно створений'
        })

    @staticmethod
    @app.route('/create_users')
    def create_users():
        mongo.db.users.insert_many([
        {
            'login': 'ivanenko',
            'pwd': '5255fda4412aef0c6d34b67593fa24e3',
            'email': 'ivanenko@ukr.net',
            'reg_date': strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'Standart_User'
        }, {
            'login': 'petrenko',
            'pwd': '24e83c25c5247423cbb48e34bb08f044',
            'email': 'petrenko@ukr.net',
            'reg_date': strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'Standart_User'
        }, {
            'login': 'sydorenko',
            'pwd': 'bede24e19e7931309d443efc0fe593c6',
            'email': 'sydorenko@ukr.net',
            'reg_date': strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'Standart_User'
        }])
        return render_template('demo/create_users.html', context={
            'msg': 'Група користувачів успішно створено'
        })

    @staticmethod
    @app.route('/read_users')
    def read_users():
        users = mongo.db.users.find()
        users_ouput = [{
            'login': user['login'],
            'pwd': user['pwd'],
            'email': user['email'],
            'reg_date': user['reg_date'],
            'status': user['status']
        } for user in users]
        return render_template('demo/read_users.html', context={
            'all_users': users_ouput
        })

    @staticmethod
    @app.route('/check_user')
    def check_user():
        return render_template('demo/check_user.html')

    @staticmethod
    @app.route('/update_user')
    def update_user():
        return render_template('demo/update_user.html')

    @staticmethod
    @app.route('/delete_user')
    def delete_user():
        return render_template('demo/delete_user.html')