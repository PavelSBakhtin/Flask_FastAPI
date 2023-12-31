# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)


# запуск из терминала: flask --app ./Lesson_1/lesson1_task1.py run
