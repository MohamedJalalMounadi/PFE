from flask import render_template, flash, redirect, url_for
from PFE import APP, bcrypt
from PFE.Forms import LoginForm
from PFE.Model import Client, Compte
from flask_login import login_user, current_user, logout_user
import datetime
import locale


@APP.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('situation_financiere'))
    form = LoginForm()
    if form.validate_on_submit():
        client = Client.query.filter_by(Login=form.login.data).first()
        if client and bcrypt.check_password_hash(
                    client.MotDePass, form.mdp.data):
            login_user(client, remember=form.remember.data)
            return redirect(url_for('situation_financiere'))
        else:
            flash(f'login or password error ! ', 'danger')
    return render_template('Authentification.html', form=form)


@APP.route("/home")
def home():
    return render_template('situation_financiere.html')


@APP.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@APP.route("/situation_financiere")
def situation_financiere():
    compt = Compte.query.filter_by(client_id=current_user.id).first()
    locale.setlocale(locale.LC_TIME, '')
    date = datetime.datetime.now()
    return render_template('situation_financiere.html', cmpt=compt, date=date)
