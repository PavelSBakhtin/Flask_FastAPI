# Написать функцию, которая будет выводить на экран HTML страницу
# с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('base.html') # напрямую
    return render_template('index.html') # через наследование


if __name__ == '__main__':
    app.run()
