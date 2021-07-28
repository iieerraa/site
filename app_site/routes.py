# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, make_response
from app_site import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/sign_up', methods=['post', 'get'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('psw')
        repeat_pas = request.form.get('psw_repeat')
        if password == repeat_pas:
            with open('users.txt', 'a') as file_handler:
                file_handler.write(f"{username};{password}\r\n")
            flash('Регистрация успешна', category='success')
        else:
            flash('Пароли не совпадают', category='error')

    return render_template('sign_up.html', title='Sign Up')


@app.route('/sign_in/', methods=['post', 'get'])
def sign_in():
    if request.method == 'POST':
        flag = False
        username = request.form.get('email')
        password = request.form.get('psw')
        file_handler = open('users.txt')
        for line in file_handler:
            file_username, file_password = line.strip().split(';', 1)
            if file_username == username and file_password == password:
                flag = True
                break
        if flag:
            cookie = make_response(render_template('user.html', user=username))
            cookie.set_cookie('user_email', username, max_age=10)
            return cookie
            # return redirect(url_for('user', user_email=username), 301)
            # flash('Авторизация успешна', category='success')
        else:
            flash('Пользователь не найден', category='error')
    return render_template('sign_in.html', title='Sign In')


@app.route('/user/')
def user():
    user_email = request.cookies.get('user_email')
    return render_template('user.html', user=user_email)


# @app.route('/user/<user_email>')
# def user(user_email=None):
#     return render_template('user.html', title=user_email)


@app.errorhandler(404)
def page_not_found(error):
    return 'Страница не найдена', 404


# @app.route('/test')
# def test():
#     return render_template('test.html', title='test')
