from flask import render_template, session, redirect, url_for, current_app
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@main.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')
