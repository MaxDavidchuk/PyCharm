from config import mysql


class Client(object):

    @staticmethod
    def check_log_mail(query: str) -> bool:
        """======================
            Перевірка зайнятості login або Email
            ====================== """
        cur = mysql.get_db().cursor()
        if '@' in query:
            sql_query = 'select id from clients where email = %s'
        else:
            sql_query = 'select id from clients where login = %s'
        return False if cur.execute(sql_query, [query]) == 1 else True

    @staticmethod
    def register(login: str, passw: str, email: str, regdate: str, role_id: int) -> str:
        """ ======================
            Реєстрація користувача
            ====================== """
        msg = ''
        conn = mysql.get_db()
        cur = conn.cursor()
        if cur.execute('select id from clients where login = %s', (login,)) == 1:
            msg += f'Логін: {login} - вже існує.\n'

        cur = conn.cursor()
        if cur.execute('select id from clients where email = %s', (email,)) == 1:
            msg += f'E-mail: {email} - вже існує.'

        if not msg:
            msg = 'ok'

        if msg == 'ok':
            sql_query = """
                insert into clients (login, passw, email, regdate, role_id)
                values (%s, %s, %s, %s, %s)
            """
            cur = conn.cursor()
            cur.execute(sql_query, (login, passw, email, regdate, role_id))
            conn.commit()
        cur.close()
        conn.close()
        return msg

    @staticmethod
    def authorize(login: str, passw: str) -> bool:
        """ =======================
            Перевірка логіна та пароля
            ======================= """
        sql_query = """
            select * from clients
            where login = %s and passw = %s
        """
        conn = mysql.get_db()
        cur = conn.cursor()
        res = cur.execute(sql_query, (login, passw))
        cur.close()
        conn.close()
        return res == 1

    @staticmethod
    def get_clients(role='All users') -> list:
        """=======================================
            Отримання списку користувачів
           ======================================= """
        conn = mysql.get_db()
        cur = conn.cursor()
        sql_query = """
            select c.id, c.login, c.email, c.regdate, r.name
            from clients c inner join roles r
            on c.role_id = r.id
        """
        cur.execute(sql_query)
        clients_list = list()
        for row in cur.fetchall():
            clients_list.append({
                'id': row[0], 'login': row[1], 'email': row[2],
                'regdate': row[3], 'role': row[4]
            })
        # cur.close()
        # conn.close()
        return clients_list

    @staticmethod
    def get_select(role: str) -> list:
        """=======================================
            Отримання списку користувачів
           ======================================= """
        conn = mysql.get_db()
        cur = conn.cursor()
        sql_query = """
            select c.id, c.login, c.email, c.regdate, r.name
            from clients c inner join roles r
            on c.role_id = r.id
            where r.name = %s
        """
        cur.execute(sql_query, [role])
        clients_list = list()
        for row in cur.fetchall():
            clients_list.append({
                'id': row[0], 'login': row[1], 'email': row[2],
                'regdate': row[3], 'role': row[4]
            })
        # cur.close()
        # conn.close()
        return clients_list

    @staticmethod
    def get_name(cid) -> str:
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select login from clients where id=%s', [cid])
        return cur.fetchone()[0]

    @staticmethod
    def get_role(cid) -> str:
        query = """
            select r.name
            from clients c inner join roles r
            on c.role_id = r.id
            where c.id = %s
        """
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute(query, [cid])
        return cur.fetchone()[0]


