from flask import render_template, flash, redirect, url_for
from PFE import APP, bcrypt
from PFE.Forms import LoginForm
from PFE.Model import Client


@APP.route("/", methods=['GET', 'POST'])
def hello():

    form = LoginForm()
    if form.validate_on_submit():
        client = Client.query.filter_by(Login=form.login.data).first()
        if client and bcrypt.check_password_hash(
                    client.MotDePass, form.mdp.data):
            flash(f'connexion succeed  {form.login.data} ! ', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'login or password error ! ', 'danger')
    return render_template('Authentification.html', form=form)


@APP.route("/home")
def home():
    return render_template('situation_financiere.html')


@APP.route("/situation_financiere")
def situation_financiere():
    return render_template('situation_financiere.html')
