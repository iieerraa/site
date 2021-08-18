# -*- coding: utf-8 -*-
import os

from flask import render_template, request, flash, redirect, url_for, session, g
from werkzeug.utils import secure_filename

from app_site import app
from app_site.FDataBase import FDataBase
from app_site.create_db import connect_db
from werkzeug.security import generate_password_hash, check_password_hash


# Работа с соединением, подключением и закрытием запросов к БД
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


dbase = None


@app.before_request
def before_request():
    """
    Установка соединения с БД перед выполнением запроса
    """
    global dbase
    db = get_db()
    dbase = FDataBase(db)


# Обработка обращений
@app.route('/')
@app.route('/index')
def index():
    """
    Главная страница
    """
    return render_template('index.html', title='Index', menu=dbase.get_menu())


@app.route('/sign_up/', methods=['post', 'get'])
def sign_up():
    """
    Регистрация пользователя
    """
    if request.method == 'POST':  # получение и обработка данных о пользователе
        if request.form.get('psw') == request.form.get('psw_repeat'):  # проверка паролей идентичности паролей
            hash_psw = generate_password_hash(request.form.get('psw'))  # хеширование пароля
            res = dbase.add_user(request.form.get('name'), request.form.get('email'), hash_psw)  # передача данных пользователя для записи в БД
            if res:
                flash('Регистрация прошла успешно', category='success')
                return redirect(url_for('sign_in'))  # перенаправление зарегистрированного пользователя на страницу пользователей
            else:
                flash('Пользователь с данным email уже зарегистрирован', category='error')
        else:
            flash('Пароли не совпадают', category='error')
    return render_template('sign_up.html', title='Sign Up', menu=dbase.get_menu())


@app.route('/sign_in/', methods=['post', 'get'])
def sign_in():
    """
    Аутентификация пользователя
    """
    if request.method == 'POST':
        try:
            user_date = dbase.get_user(request.form.get('email'))  # данные пользователя time, name, email, psw
            if check_password_hash(user_date['psw'], request.form.get('psw')):  # проверка хеша пароля
                session['user'] = user_date['name']
                session['user_id'] = user_date['time']
                return redirect(url_for('user'))
            else:
                flash('Пароль не введён не верно', category='error')
        except:
            flash('Пользователь не найден', category='error')
    return render_template('sign_in.html', title='Sign In', menu=dbase.get_menu())


# Связать проверку расширения принимаемого файла с конфигурацией
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ['jpg', 'jpeg', 'gif', 'png']  # ALLOWED_EXTENSIONS


@app.route('/user/', methods=['post', 'get'])
def user():
    """
    Страница пользователя
    """
    if "user" in session:
        username = session['user']
        user_id = session['user_id']
        if request.method == 'POST':
            photo = request.files['photo']
            if photo and allowed_file(photo.filename):
                filename = secure_filename(photo.filename)
                # НЕРАБОТАЕТ ЗАРАЗА ТАКАЯ ЕДРИЧЕСКАЯ ПОПЕРЁК ХРЕБТА ЕЁ БЫ ДОЛБАНУТЬ!!!!
                # ОСТАЛОСЬ ТОЛЬКО ЗАДНИЦУ К ЭКРАНУ ПРИСЛОНИТЬ!!!!
                # VVVVVVVVVVVVVVVVVVVVVVVVVV
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Я НЕ ХОЧУ РОБКОТОТЬ!!!!
                # ^^^^^^^^^^^^^^^^^^^^^^^^^
                # ПАКОСТЬ!!!!!!!!!!!!!
                # try:
                #     photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #     dbase.add_post(user_id, request.form.get('post'), filename)
                #     flash('Ваша запись успешно добавлена', category='success')
                # except:
                #     print(filename)
                #     print(photo)
                #     flash('Произошла ошибка добавления записи', category='error')

        # if request.method == 'POST':
        #     # post = request.form.get('post')
        #     # photo = request.files['photo']
        #     res = dbase.add_post(user_id, request.form.get('post'), request.form.get('photo'))  # передача данных пользователя для записи в БД
        #
        #     if res:
        #         flash('Ваша запись успешно добавлена', category='success')
        #     else:
        #         flash('Произошла ошибка добавления записи', category='error')

        return render_template('user.html', user=username, menu=dbase.get_menu())
    else:
        return redirect(url_for('sign_in'))  # если пользователь не аутентифицирован, перенаправление на страницу входа


@app.route('/sign_out/')
def sign_out():
    """
    Разлогинивание пользователя
    """
    session.pop('user', None)  # Очистка сессии
    return redirect(url_for('sign_in'))


# Обработка ошибок
@app.errorhandler(404)
def page_not_found(error):
    return 'Страница не найдена', 404
