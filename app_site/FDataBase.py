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

    def add_user(self, name, email, psw):
        try:
            self.__cur.execute('SELECT COUNT() as "count" FROM user WHERE email=:e_mail;', {'e_mail': email})
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Пользователь с данным email существует', email)
                return False

            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO user VALUES(NULL, ?, ?, ?, ?);', (name, email, psw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления пользователя в БД' + str(e))
            return False
        return True

    def get_user(self, email):
        try:
            self.__cur.execute('SELECT time, name, email, psw FROM user WHERE email=:e_mail;', {'e_mail': email})
            res = self.__cur.fetchone()
            return res
        except sqlite3.Error as e:
            print("Пользователь не найден" + str(e))

        return None

    def add_post(self, user_id, post, photo=None):
        try:
            post_id = math.floor(time.time())
            self.__cur.execute('INSERT INTO content VALUES(NULL, ?, ?, ?, ?);', (user_id, post_id, post, photo))
            self.__db.commit()
            res = True
            return res
        except:
            print('Ошибка добавления поста')

    def get_post(self, user_id):
        try:
            pass
        except:
            print('Ошибка Получения поста')
