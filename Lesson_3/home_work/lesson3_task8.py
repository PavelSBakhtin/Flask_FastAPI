# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import Config
from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
csrf = CSRFProtect(app)

category = [{"title": 'Registration', "func_name": 'registration'}]

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', category=category)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User(name=name, surname=surname, email=email)
        if User.query.filter(User.email == email).first():
            flash(f'Пользователь с e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration'))
    return render_template('registration.html', form=form)
