from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/login')
def login():
    return 'Login page'


@app.route('/welcome')
def welcome():
    return 'Welcome page'