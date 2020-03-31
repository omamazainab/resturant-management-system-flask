from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True) 
    password_hash = db.Column(db.String(128))
    # products = db.relationship('product', backref='admin', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), unique=True, index=True)
    category = db.Column(db.String(64), index=True )
    description = db.Column(db.String(64), unique=True, index=True)
    price = db.Column(db.Integer, index=True)
    image = db.Column(db.String(1000), index=True)
    # admin = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __repr__(self):
        return '<Product %r>' % self.product_name
     
    