# from flask import Flask, render_template, session, redirect, url_for, escape, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# import json
# from datetime import datetime
# from flask_mail import Mail


# with open('config.json', 'r') as c:
#     params = json.load(c)["params"]

# local_server = True
# app = Flask(__name__)
# app.secret_key = "any_random_string"
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = params['gmail-user'],
#     MAIL_PASSWORD=  params['gmail-password']
# )
# mail = Mail(app)

# if(local_server):
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']




# db = SQLAlchemy(app)


# class Contacts(db.Model):
#     '''
#     sno, name phone_num, msg, date, email
#     '''
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(20), nullable=False)
#     phone_no = db.Column(db.String(12), nullable=False)
#     message = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)


# class Posts(db.Model):
#     '''
#     sno, title, slug, content, date
#     '''
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(25), nullable=False)
#     img_file = db.Column(db.String(25), nullable=False)
#     content = db.Column(db.String(1000), nullable=False)
#     date = db.Column(db.String(12), nullable=True)




    
# @app.route("/")
# def home():
#     posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
#     return render_template('index.html',params=params, posts=posts)




# @app.route("/about")
# def about():
#     return render_template('about.html',params=params)



# @app.route("/login" , methods = ['GET' , 'POST'])
# def login():
    
#     if request.method == 'POST' :
#         return redirect(url_for("about"))    
#     else:
#         return render_template("login.html",params=params)
    


# @app.route("/dashboard")
# def dashboard():
#     return render_template('dashboard.html',params=params)



# @app.route("/post/<string:post_slug>" , methods = ['GET'])
# def post_route(post_slug):
#     post = Posts.query.filter_by(slug=post_slug).first()
#     return render_template('post.html',params=params, post=post)




# @app.route("/contact", methods = ['GET' , 'POST'])
# def contact():
#     if(request.method == 'POST'):
#         # add entry to the database
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#         entry = Contacts(name=name , email = email , phone_no = phone, message = message, date= datetime.now())
#         db.session.add(entry)
#         db.session.commit()
#         mail.send_message('New message from ' + name,sender=email,recipients = ['omi.zainy@gmail.com'],body = message + "\n" + phone)
#     return render_template('contact.html',params=params)



# app.run(debug=True)

import os
import click
from app import create_app, db
from app.models import Admin
from flask_migrate import Migrate

app = create_app(os.getenv('FELICIANO_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Admin=Admin)



@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

