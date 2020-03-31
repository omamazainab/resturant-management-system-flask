from flask import render_template, session, redirect, url_for, current_app, request, flash
from . import admin
from .forms import LoginForm, RegistrationForm, ProductForm
from ..models import Admin, Product
from flask_login import login_user, logout_user, login_required, \
    current_user
from flask_login import logout_user, login_required
from werkzeug.utils import secure_filename
from .. import db
# from .. import app
import os

# @admin.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('admin/login.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin is not None and admin.verify_password(form.password.data):
            login_user(admin, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('admin.dashboard')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('admin/login.html', form=form)


@admin.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('admin/admin_dashboard.html')


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Admin(email=form.email.data,
                     username=form.username.data,
                     password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)


@admin.route('/products', methods=['GET', 'POST'])
def products():
    return 'you are not supposed to touch the itchy pimple'


@admin.route('/add-product', methods=['GET', 'POST'])
@login_required
def addProducts():
    form = ProductForm()
    if form.validate_on_submit():
        # Create a directory in a known location to save files to.
        uploads_dir = os.path.join(app.instance_path, 'uploads')
        os.makedirs(uploads_dir, exists_ok=True)
    
        form.image.data.save(os.path.join(uploads_dir, secure_filename(form.image.data.filename)))
   
        if current_user.is_authenticated:
            product=Product(product_name=form.product_name.data, category=form.category.data,
                              description=form.description.data, price=form.price.data, image=filename)
            db.session.add(product)
            db.session.commit()
    return render_template('admin/add-product.html', form=form)
