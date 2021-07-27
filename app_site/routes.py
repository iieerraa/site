# -*- coding: utf-8 -*-

from flask import render_template, request, flash
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


@app.route('/sign_in', methods=['post', 'get'])
def sign_in():
    if request.method == 'POST':
        flag = False
        username = request.form.get('email')
        password = request.form.get('psw')
        file_handler = open('users.txt')
        for line in file_handler:
            user = line.strip().split(';')
            if user[0] == username and user[1] == password:
                flag = True
                break
        if flag:
            flash('Авторизация успешна', category='success')
        else:
            flash('Пользователь не найден', category='error')
    return render_template('sign_in.html', title='Sign In')


# @app.route('/id/<int:post_id>')
# def new(post_id=None):
#     return render_template('sign_in.html', title=post_id)


# @app.route('/test')
# def test():
#     return render_template('test.html', title='test')
