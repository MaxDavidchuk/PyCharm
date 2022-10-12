from flask import render_template, request, session, redirect, make_response
from config import app
from hashlib import md5
from datetime import datetime
from models.client import Client
from models.role import Role


class AuthViews(object):

    @staticmethod
    @app.route('/auth/signup', methods=['GET', 'POST'])
    def auth_signup():
        """ Сторінка реєстрації """
        if request.method == 'GET':
            return render_template('auth/signup.html', context={})
        elif request.method == 'POST':
            login = request.form['login']
            pass1 = request.form['pass1']
            email = request.form['email']
            #
            passw = md5(pass1.encode()).hexdigest()
            regdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            res = Client().register(login, passw, email, regdate, 6)
            header = 'Звіт про реєстрацію'
            if res == 'ok':
                msg = 'Рестрацію успішно завершено!'
                color = 'green'
            else:
                msg = res
                color = 'red'
            return render_template('auth/report.html', context={
                'res_msg': msg,
                'res_header': header,
                'res_color': color
            })

    @staticmethod
    @app.route('/auth/signin', methods=['GET', 'POST'])
    def auth_signin():
        """ Сторінка авторизації """
        if request.method == 'GET':
            return render_template('auth/signin.html', context={})
        elif request.method == 'POST':
            login = request.form['login']
            passw = request.form['passw']
            passw = md5(passw.encode()).hexdigest()
            #
            client_model = Client()
            if client_model.authorize(login, passw):
                msg = 'Авторизацію успішно завершено!'
                color = 'green'
                session['user'] = login
            else:
                msg = 'Користувач не знайдений!'
                color = 'red'
            #
            return render_template('auth/report.html', context={
                'res_header': 'Звіт про авторизацію',
                'res_msg': msg,
                'res_color': color
            })

    @staticmethod
    @app.route('/auth/signout')
    def auth_signout():
        """ Сторінка виходу із систему """
        session.pop('user')
        # return render_template('auth/signout.html', context={})
        return redirect('/')

    @staticmethod
    @app.route('/auth/profile')
    def auth_profile():
        """ Сторінка профіля користувача """
        return render_template('auth/profile.html', context={})

    @staticmethod
    @app.route('/auth/ajax')
    def auth_ajax():
        req = request.args.get('login') if request.args.get('login') else request.args.get('email')
        msg = True if Client().check_log_mail(req) else False
        return { 'msg': msg }

    @staticmethod
    @app.route('/auth/admin', methods=['GET', 'POST'])
    def auth_admin():
        """ Сторінка адміністратора """
        c_model = Client()
        r_model = Role()
        if request.method == 'GET':
            if 'user' in session  and session['user'] == 'admin123':
                return render_template('auth/admin.html', context={
                    'all_clients': c_model.get_clients('All users'),
                    'all_roles': r_model.get_roles(),
                    'msg': ''
                })
            else:
                return make_response(render_template('auth/403.html'), 403)
        elif request.method == 'POST':
            role = request.form['role']
            return render_template('auth/admin.html', context={
                    'all_clients': c_model.get_clients(role),
                    'all_roles': r_model.get_roles(),
                    'msg': f'Обрана роль: {role}'
                })

    @staticmethod
    @app.route('/auth/editor/<cid>', methods=['GET', 'POST'])
    def auth_editor(cid):
        """ Сторінка редагування користувача """
        c_model = Client()
        r_model = Role()
        if request.method == 'GET':
            if 'user' in session  and session['user'] == 'admin123':
                return render_template('auth/editor.html', context={
                    'all_roles': r_model.get_roles(),
                    'user_name': c_model.get_name(cid),
                    'user_role': c_model.get_role(cid),
                    'user_id': cid
                })
            else:
                return make_response(render_template('auth/403.html'), 403)
        elif request.method == 'POST':
            role = request.form['role']
            return render_template('auth/admin.html', context={
                    'all_clients': c_model.get_clients(role),
                    'all_roles': r_model.get_roles(),
                    'msg': f'Обрана роль: {role}'
                })

    @staticmethod
    @app.route('/auth/ajax_editor')
    def auth_ajax_editor():
        msg = Client().change_role(request.args.get('user'), request.args.get('role'))
        return {'msg': msg}
