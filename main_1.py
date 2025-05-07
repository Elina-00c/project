from flask import Flask, render_template, redirect
from forms.Loginform import LoginForm
from forms.RegisterForm import RegisterForm
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/users.sqlite')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Домашняя страница', username='username')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if not db_sess.query(User).filter(User.nickname == form.nickname.data).first():
            return render_template('login.html', title='Регистрация',
                                   form=form,
                                   message="Такого пользователя нет")
        if not db_sess.query(User).filter(User.password == form.password.data).first():
            return render_template('login.html', title='Регистрация',
                                   form=form,
                                   message="Неверный пароль")
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def login1():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.nickname == form.nickname.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Такой никнейм уже есть")
        elif db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Такая почта уже есть")
        elif db_sess.query(User).filter(User.password == form.password.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Такой пароль уже есть")
        user = User(
            nickname=form.nickname.data,
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/success')
def main():
    return render_template('shop.html', title='Домашняя страница')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
