from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def reg():
    return render_template('myprojects.html')


@app.route('/myprojects')
def index():
    return render_template('myprojects.html')


@app.route('/chats')
def chats():
    return render_template('chats.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/mail')
def mail():
    return render_template('mail.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        login = request.form.get('login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute(f'SELECT password FROM passwords WHERE login = "{login}";')
        pas = cursor_db.fetchall()

        cursor_db.close()
        try:
            if pas[0][0] != Password:
                return render_template('auth_bad.html')
        except Exception:
            return render_template('auth_bad.html')

        db_lp.close()
        return render_template('successfulauth.html')

    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def form_registration():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        sql_insert = '''INSERT INTO passwords VALUES('{}','{}');'''.format(Login, Password)
        cursor_db.execute(sql_insert)

        cursor_db.close()

        db_lp.commit()
        db_lp.close()

        return render_template('successfulregis.html')

    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
