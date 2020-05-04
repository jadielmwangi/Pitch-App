from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User
from .forms import  LoginForm,RegistrationForm
from .. import db
from ..email import mail_message
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    title = "Pitch login"
    return render_template('auth/login.html',login_form = login_form, title = title)
