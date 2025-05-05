from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# здесь будет база данных
# db_session.global_init('mars_explorer.sqlite')
# db_sess = db_session.create_session()
# colonists = db_sess.query(User).all()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Домашняя страница', username='username')


@app.route('/login', methods=['GET', 'POST'])
def registration():
    return render_template('login.html')


@app.route('/registration')
def login1():
    return render_template('registration.html')


@app.route('/success')
def main():
    return render_template('index.html', title='Домашняя страница')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
