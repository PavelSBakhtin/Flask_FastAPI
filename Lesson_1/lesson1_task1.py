# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(name)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if name == 'main':
    app.run()
