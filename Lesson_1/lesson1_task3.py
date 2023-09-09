# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/sum-nums/<int:num1>/<int:num2>/')
def sum_nums(num1, num2):
    # return str(num1 + num2)
    return str(f'{num1} + {num2} = {num1 + num2}')


if __name__ == '__main__':
    app.run()
