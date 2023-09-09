# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('x_index.html')


@app.route('/about/')
def about():
    return render_template('x_about.html')


@app.route('/contact/')
def contact():
    return render_template('x_contact.html')


@app.route('/students/')
def students():
    _students = [
        {
            "name": "John",
            "surname": "Doe",
            "age": 20,
            "average": 85
        },
        {
            "name": "Jane",
            "surname": "Smith",
            "age": 22,
            "average": 92
        },
    ]
    context = {'students': _students}
    return render_template('x_students.html', **context)


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
    return render_template('x_news.html', **context)


if __name__ == '__main__':
    app.run()
