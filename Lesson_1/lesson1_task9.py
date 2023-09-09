# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('9_index.html')


@app.route('/cloth/')
def cloth():
    return render_template('9_cloth.html')


@app.route('/cost1/')
def cost1():
    return render_template('9_cost1.html')


@app.route('/cost2/')
def cost2():
    return render_template('9_cost2.html')


@app.route('/cost3/')
def cost3():
    return render_template('9_cost3.html')


@app.route('/jackets/')
def jackets():
    return render_template('9_jackets.html')


@app.route('/jack1/')
def jack1():
    return render_template('9_jack1.html')


@app.route('/jack2/')
def jack2():
    return render_template('9_jack2.html')


@app.route('/jack3/')
def jack3():
    return render_template('9_jack3.html')


@app.route('/shoes/')
def shoes():
    return render_template('9_shoes.html')


@app.route('/shoe1/')
def shoe1():
    return render_template('9_shoe1.html')


@app.route('/shoe2/')
def shoe2():
    return render_template('9_shoe2.html')


@app.route('/shoe3/')
def shoe3():
    return render_template('9_shoe3.html')


if __name__ == '__main__':
    app.run()
