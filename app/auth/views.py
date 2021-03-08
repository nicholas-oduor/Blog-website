from . import auth
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User,Writer
from ..request import get_quote
from .forms import LoginForm,RegistrationForm,WriterRegistrationForm,WriterLoginForm
from .. import db
from ..email import mail_message


@auth.route('/login/user',methods=['GET','POST'])
def login():
    quote = get_quote()
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Nicholas blog website"
    return render_template('auth/login.html',login_form = login_form,title=title, quote=quote)

def writer_login():
    quote = get_quote()
    login_form = WriterLoginForm()
    if login_form.validate_on_submit():
        writer = Writer.query.filter_by(writer_email = login_form.writer_email.data).first()
        if writer is not None and writer.verify_password(login_form.password.data):
            login_user(writer,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Nicholas blog website"
    return render_template('auth/writer_login.html',login_form = login_form,title=title, quote=quote)
