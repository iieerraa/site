import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения БД')
        return []

    def add_user(self, email, psw):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO user VALUES(NULL, ?, ?, ?);', (email, psw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления пользователя в БД' + str(e))
            return False
        return True

    def get_user(self, username, password):
        try:
            self.__cur.execute('SELECT time FROM user WHERE email=:e_mail AND psw=:passw;', {'e_mail': username, 'passw': password})
            rows = self.__cur.fetchone()
            res = None
            if rows:
                res = []
                for row in rows:
                    res.append(row)
            if res:
                return res
        except sqlite3.Error as e:
            print("Пользователь не найден" + str(e))

        return None
