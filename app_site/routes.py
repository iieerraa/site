# -*- coding: utf-8 -*-

from flask import render_template
from app_site import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')


@app.route('/new/')
@app.route('/new/<int:post_id>')
def new(post_id=None):
    return render_template('new.html', title=post_id)
