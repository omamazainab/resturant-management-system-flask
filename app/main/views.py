from flask import render_template, session, redirect, url_for, current_app
from . import main
from ..models import Product

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@main.route('/menu', methods=['GET', 'POST'])
def menu():
    categories = ['breakfast','lunch','dinner','drinks','desserts']
    products = Product.query.filter_by().all()
    return render_template('menu.html', categories = categories, products = products )
