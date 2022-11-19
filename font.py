from crypt import methods
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import os
from flask_sqlalchemy import SQLAlchemy # Started wotking with Database
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

#Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  #Database set

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(id=Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123'

@app.route('/second')
def index():
    return render_template('first.html', methods=['GET', 'POST'])

@app.route('/')
def first():
    return render_template('second.html', methods=['GET', 'POST'])