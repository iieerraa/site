# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, make_response, session
from app_site import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/sign_up/', methods=['post', 'get'])
def sign_up():  # регистрация пользователя
    if request.method == 'POST':  # получение и обработка данных о пользователе
        username = request.form.get('email')
        password = request.form.get('psw')
        repeat_pas = request.form.get('psw_repeat')
        if password == repeat_pas:
            with open('users.txt', 'a') as file_handler:  # открытие файла с данными пользователей для дозаписи
                file_handler.write(f"{username};{password}\r\n")  # запись данных о новом пользователе в файл
            session['user'] = username  # запись емайла пользователя в сессию
            return redirect(url_for('user'))  # перенаправление зарегистрированного пользователя на страницу пользователей
            # flash('Регистрация успешна', category='success')
        else:
            flash('Пароли не совпадают', category='error')
    return render_template('sign_up.html', title='Sign Up')


@app.route('/sign_in/', methods=['post', 'get'])
def sign_in():  # аутентификация пользователя
    if request.method == 'POST':  # получение и обработка данных о логине и пароле
        username = request.form.get('email')
        password = request.form.get('psw')
        file_handler = open('users.txt')  # открытие файла с данными пользователей для чтения
        for line in file_handler:  # построчное чтение файла с данными пользователей
            file_username, file_password = line.strip().split(';', 1)
            if file_username == username and file_password == password:
                session['user'] = username  # запись емайла пользователя в сессию
                return redirect(url_for('user'))  # перенаправление вошедшего пользователя на страницу пользователей
                # cookie = make_response(render_template('user.html', user=username))
                # cookie.set_cookie('user_email', username, max_age=10)
                # return cookie
            # return redirect(url_for('user', user_email=username), 301)
            # flash('Авторизация успешна', category='success')
        flash('Пользователь не найден', category='error')
    return render_template('sign_in.html', title='Sign In')


@app.route('/user/')
def user():  # страница аутентифицированного пользователя
    if "user" in session:
        username = session["user"]
        return render_template('user.html', user=username)
    else:
        return redirect(url_for('sign_in'))  # если пользователь не аутеентифицирован, перенаправление на страницу входа
    # user_email = request.cookies.get('user_email')
    # return render_template('user.html', user=user_email)


@app.route('/sign_out/')
def sign_out():
    session.pop('user', None)
    return redirect(url_for('sign_in'))

# @app.route('/user/<user_email>')
# def user(user_email=None):
#     return render_template('user.html', title=user_email)


@app.errorhandler(404)
def page_not_found(error):
    return 'Страница не найдена', 404


# @app.route('/test')
# def test():
#     return render_template('test.html', title='test')
