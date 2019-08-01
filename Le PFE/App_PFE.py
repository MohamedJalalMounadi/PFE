from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Forms import LoginForm
from flask_login import LoginManager
APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'e1629760ff816b5f25223835689744dd'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/myPFE'
DB = SQLAlchemy(APP)
LM = LoginManager(APP)


class Client(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    Nom = DB.Column(DB.String(40), nullable=False)
    Prenom = DB.Column(DB.String(40), nullable=False)
    DateNaissance = DB.Column(DB.String(20), nullable=False)
    Telephone = DB.Column(DB.String(20), nullable=False)
    Email = DB.Column(DB.String(120), nullable=False)
    Login = DB.Column(DB.String(20), nullable=False)
    MotDePass = DB.Column(DB.String(60), nullable=False)


@APP.route("/", methods=['GET', 'POST'])
def hello():

    form = LoginForm()
    if form.validate_on_submit():
        if form.login.data == 'admin@admin.com'and form.mdp.data == 'mounadi56':
            flash(f'connexion succeed  {form.login.data} ! ', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'login or password error ! ', 'danger')
    return render_template('Authentification.html', form=form)


@APP.route("/home")
def home():
    return render_template('Home.html')


@APP.route("/situation_financiere")
def situation_financiere():
    return render_template('situation_financiere.html')


if __name__ == '__main__':
    APP.run(debug=True)
