# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/str_len/<str_inp>/')
def str_len(str_inp):
    return str(len(str_inp))


if __name__ == '__main__':
    app.run()
