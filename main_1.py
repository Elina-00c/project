from flask import Flask, render_template, redirect
from forms.Loginform import LoginForm
from forms.RegisterForm import RegisterForm
from forms.OfficeForm import OfficeForm
from forms.FindForm import FindForm
from data.users import User
from data.products import Product
from data import db_session
import sys
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/shops.sqlite')
db_sess = db_session.create_session()
for i in db_sess.query(Product).filter(Product.name == 'Book'):
    print(i.id)


def map_image():
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.681281,55.677089&spn=0.01,0.01&size=600,450&l=map&pt=37.681281,55.677089,pm2pnm~37.681281,55.677089,pm2pnm"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "static/img/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


map_image()


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


@app.route("/office", methods=['GET', 'POST'])
def my_office():
    """
    Обработка страницы профиля
    :return: страничка user
    """
    form = OfficeForm()
    if form.validate_on_submit():
        form.nickname.data = "Scott"
        form.name.data = "name"
        form.email.data = "email"
        form.password.data = "password"
        return redirect('/office')
    return render_template('office.html', title='Ваш аккаунт', form=form)


@app.route('/find', methods=['GET', 'POST'])
def find():
    form = FindForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        products_db = db_sess.query(Product).all()
        names = [product.name for product in products_db]
        prices = [product.price for product in products_db]
        providers = [product.provider for product in products_db]
        types = [product.type for product in products_db]
        if db_sess.query(Product).filter(Product.name == form.find.data).first():
            result = []
            id = []
            for i in db_sess.query(Product).filter(Product.name == form.find.data):
                id.append(i.id)
            for index in id:
                stroka = (f"Название: {names[index - 1]}, Цена: {prices[index - 1]}, Поставщик: {providers[index - 1]}, "
                          f"Тип продукта: {types[index - 1]}")
                result.append(stroka)
            return render_template('find.html', title='Поиск товаров',
                                   form=form, news=result)

        return redirect('/success')

    return render_template('find.html', title='Поиск товаров', form=form)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
