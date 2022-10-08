from config import mysql


class Role(object):

    @staticmethod
    def get_roles() -> list:
        """=======================================
            Отримання повного списку ролей
           ======================================= """
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select * from roles order by id')
        roles_list = list()
        for row in cur.fetchall():
            roles_list.append({'id': row[0], 'name': row[1]})
        # cur.close()
        # conn.close()
        return roles_list
