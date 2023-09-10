from flask import Flask, render_template, request
from models import db, Users
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

from flask_wtf.csrf import CSRFProtect

app.config['SECRET_KEY'] = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username = form.username.data
    email = form.email.data
    password = form.password.data
    if request.method == 'POST' and form.validate():
        if Users.query.filter(Users.username == username).all() or Users.query.filter(Users.email == email).all():
            context = {'alert_message': "Пользователь уже существует!"}
            return render_template('login.html', form=form, **context)
        else:
            print(Users.query.filter(Users.username == username).all())
            new_user = Users(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
    return render_template('login.html', form=form)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    context = {'alert_message': "Добро пожаловать!"}
    form = RegistrationForm()
    username = form.username.data
    email = form.email.data
    password = form.password.data
    birthday = form.birthday.data
    terms = form.terms.data
    if request.method == 'POST' and form.validate():
        if Users.query.filter(Users.username == username).all() or Users.query.filter(Users.email == email).all():
            context = {'alert_message': "Пользователь уже существует!"}
            return render_template('registration.html', form=form, **context)
        else:
            print(Users.query.filter(Users.username == username).all())
            new_user = Users(username=username, email=email, password=password, birthday=birthday, terms=terms)
            db.session.add(new_user)
            db.session.commit()
            return render_template('registration.html', form=form, **context)
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run()
