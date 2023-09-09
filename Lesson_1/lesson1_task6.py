# Написать функцию, которая будет выводить на экран HTML страницу с таблицей,
# содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


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
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
