from flask import render_template, session, request
from config import app, mongo
from time import strftime
from hashlib import md5


class TaskViews(object):

    @staticmethod
    @app.route('/task/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('task/create.html')
        elif request.method == 'POST':
            count = request.form['tab-count']
            if count == '2':
                mongo.db.list.insert_one({
                    'todo': request.form['new-task1'],
                    'start': request.form['s-date1'],
                    'finish': request.form['f-date1'],
                    'status': 'New task'
                })
                return render_template('task/show.html', context={
                    'msg': 'Task was added successfuly!'
                })


    @staticmethod
    @app.route('/task/creates', methods=['GET', 'POST'])
    def creates():
        if request.method == 'GET':
            return render_template('task/creates.html', context={
                'msg': 'Група користувачів успішно створено'
            })
        elif request.method == 'POST':
            tab_count = int(request.form['tab-count']) - 1
            if tab_count == 1:
                pass
            else:
                pass

    @staticmethod
    @app.route('/task/show')
    def read_users():
        todo_list = mongo.db.list.find()
        list_ouput = [{
            'id': todo['_id'],
            'todo': todo['todo'],
            'start': todo['start'],
            'finish': todo['finish'],
            'status': todo['status']
        } for todo in todo_list]
        return render_template('task/show.html', context={
            'task_list': list_ouput
        })

    @staticmethod
    @app.route('/task/edit')
    def update_user():
        return render_template('task/edit.html')

    @staticmethod
    @app.route('/task/delete')
    def delete_user():
        return render_template('task/delete.html')