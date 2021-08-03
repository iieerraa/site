# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, session, g
from app_site import app
from app_site.FDataBase import FDataBase
from app_site.create_db import connect_db


@app.route('/')
@app.route('/index')
def index():
    """
    Главная страница
    """
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title='Index', menu=dbase.get_menu())


@app.route('/sign_up/', methods=['post', 'get'])
def sign_up():
    """
    Регистрация пользователя
    """
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':  # получение и обработка данных о пользователе
        username = request.form.get('email')
        password = request.form.get('psw')
        repeat_pas = request.form.get('psw_repeat')
        if password == repeat_pas:
            res = dbase.add_user(username, password)
            session['user'] = username  # запись емайла пользователя в сессию
            return redirect(url_for('user'))  # перенаправление зарегистрированного пользователя на страницу пользователей
        else:
            flash('Пароли не совпадают', category='error')
    return render_template('sign_up.html', title='Sign Up', menu=dbase.get_menu())


@app.route('/sign_in/', methods=['post', 'get'])
def sign_in():
    """
    Аутентификация пользователя
    """
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':  # получение и обработка данных о логине и пароле
        username = request.form.get('email')
        password = request.form.get('psw')
        user_id = dbase.get_user(username, password)
        if not user_id:
            flash('Пользователь не найден', category='error')
        else:
            session['user'] = user_id
            return redirect(url_for('user'))
        # file_handler = open('users.txt')  # открытие файла с данными пользователей для чтения
        # for line in file_handler:  # построчное чтение файла с данными пользователей
        #     file_username, file_password = line.strip().split(';', 1)
        #     if file_username == username and file_password == password:
        #         session['user'] = username  # запись емайла пользователя в сессию
        #         return redirect(url_for('user'))  # перенаправление вошедшего пользователя на страницу пользователей
        # flash('Пользователь не найден', category='error')
    return render_template('sign_in.html', title='Sign In', menu=dbase.get_menu())


@app.route('/user/')
def user():
    """
    Страница пользователя
    """
    db = get_db()
    dbase = FDataBase(db)
    if "user" in session:
        username = session["user"]
        return render_template('user.html', user=username, menu=dbase.get_menu())
    else:
        return redirect(url_for('sign_in'))  # если пользователь не аутеентифицирован, перенаправление на страницу входа


@app.route('/sign_out/')
def sign_out():
    """
    Разлогинивание пользователя
    """
    session.pop('user', None)
    return redirect(url_for('sign_in'))


@app.errorhandler(404)
def page_not_found(error):
    return 'Страница не найдена', 404


def get_db():
    """
    Соединение с БД
    """
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """
    Закрытие соединения с БД
    """
    if hasattr(g, 'link_db'):
        g.link_db.close()
