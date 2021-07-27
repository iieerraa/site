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


@app.route('/sing_in.html', methods=['post', 'get'])
def sign_in():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('psw')
        if username == 'login' and password == 1234:
            pass
        else:
            flash('Пользователь не найден', category='error')

    return render_template('sign_in.html', title='Sign In')


@app.route('/id/<int:post_id>')
def new(post_id=None):
    return render_template('sign_in.html', title=post_id)
