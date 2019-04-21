from flask import Flask, redirect, url_for

app = Flask(__name__)

credentials = ('admin', 'admin')

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return 'Login page'


@app.route('/welcome')
def welcome():
    return 'Welcome page'