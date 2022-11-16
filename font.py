from crypt import methods
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123'

@app.route('/second')
def index():
    return render_template('first.html', methods=['GET', 'POST'])

@app.route('/')
def first():
    return render_template('second.html', methods=['GET', 'POST'])