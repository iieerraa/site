# -*- coding: utf-8 -*-

from flask import render_template, request
from app_site import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/sign_up', methods=['post', 'get'])
def sign_up():
    message = ''
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('psw')
        repeat_pas = request.form.get('psw_repeat')
        message = 'Ok'

    return render_template('sign_up.html', title='Sign Up', message=message)


@app.route('/id/<int:post_id>')
def new(post_id=None):
    return render_template('new.html', title=post_id)
