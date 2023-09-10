from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp


class LoginForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


# Создайте форму регистрации пользователя с использованием Flask-WTF.
# Форма должна содержать следующие поля:
# - Имя пользователя (обязательное поле);
# - Электронная почта (обязательное поле, с валидацией на корректность ввода email);
# - Пароль (обязательное поле, с валидацией на минимальную длину пароля);
# - Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем).
# После отправки формы данные должны сохраняться в базе данных
# (можно использовать SQLite) и выводиться сообщение об успешной регистрации.
# Если какое-то из обязательных полей не заполнено или данные не прошли валидацию,
# то должно выводиться соответствующее сообщение об ошибке.
# Дополнительно:
# - добавьте проверку на уникальность имени пользователя и электронной почты в базе данных;
# - если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8),
                                                     Regexp('(?=.*[a-z])(?=.*[0-9])',
                                                     message="Ошибка! Нужны цифры и буквы!")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    birthday = DateTimeField('Birthday (dd.mm.yyyy)', format='%d.%m.%Y')
    terms = BooleanField("I'm agree with terms conditions and privacy policy.", validators=[DataRequired()])


# Дополняем прошлую задачу:
# Создайте форму для регистрации пользователей в вашем веб-приложении.
# Форма должна содержать следующие поля: имя пользователя, электронная почта, пароль и подтверждение пароля.
# Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
# После отправки формы, выведите успешное сообщение об успешной регистрации.

# Создайте форму регистрации пользователей в приложении Flask.
# Форма должна содержать поля: имя, фамилия, email, пароль и подтверждение пароля.
# При отправке формы данные должны валидироваться на следующие условия:
# - Все поля обязательны для заполнения;
# - Поле email должно быть валидным email адресом;
# - Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру;
# - Поле подтверждения пароля должно совпадать с полем пароля;
# - Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка;
# - Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.
