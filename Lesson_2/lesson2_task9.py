# Создать страницу, на которой будет форма для ввода имени и электронной почты.
# При отправке которой будет создан cookie файл с данными пользователя.
# Также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти".
# При нажатии на кнопку будет удален cookie файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request,  make_response

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'main'}
    return render_template('9_index.html', **context)


@app.route('/log_in/', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        context = {'title': 'main', 'name': request.form.get('login')}
        name = request.form.get('login')
        response = make_response(render_template('9_index.html', **context))
        response.set_cookie(name, 'admin')
        return response
    context = {'title': 'login'}
    return render_template('9_login.html', **context)


@app.route('/log_out/')
def log_out():
    context = {'title': 'login'}
    response = make_response(render_template('9_index.html', **context))
    response.set_cookie(*request.cookies, expires=0)
    return response


if __name__ == '__main__':
    app.run()
