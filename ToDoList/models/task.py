from config import app, mongo

class Task(object):

    @staticmethod
    def get_tasks() -> list:
        t_list = list
