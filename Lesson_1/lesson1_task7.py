# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/news/')
def news():
    _news = [
        {
            "title": "Qwerty",
            "descr": "Poiuy",
            "date": 201
        },
        {
            "title": "Asdfg",
            "descr": "Lkjhg",
            "date": 202
        },
        {
            "title": "Zxcvb",
            "descr": "Mnbvc",
            "date": 203
        },
    ]
    context = {'news': _news}
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run()
