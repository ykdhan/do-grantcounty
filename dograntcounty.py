from flask import Flask, render_template, flash, redirect, url_for, request, session, jsonify
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, IntegerField, PasswordField, BooleanField, HiddenField, TextAreaField
from wtforms.validators import Email, Length, NumberRange, DataRequired, InputRequired, EqualTo, AnyOf, Regexp, Optional
from flask_wtf import FlaskForm, validators
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_hashing import Hashing
from flask_mail import Mail, Message
import string, random, datetime, re, os

import db

app = Flask(__name__)
hashing = Hashing(app)

app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.mail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='dograntcounty@mail.com',
    MAIL_PASSWORD='DoDo1234!'
)

mail = Mail(app)


def send_email(recipients, title, text_body, html_body):
    msg = Message(title, sender='dograntcounty@mail.com', recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


app.config['SECRET_KEY'] = 'Do Grant County Key'
app.config['WTF_CSRF_ENABLED'] = False


@app.before_request
def before():
    db.open_db_connection()


@app.teardown_request
def after(exception):
    db.close_db_connection()


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/event', methods=["GET", "POST"])
def load_event():
    return render_template('event.html')


@app.route('/event/<year>/<month>/', methods=["GET", "POST"])
def event(year, month):
    previous = EventControlPreviousForm()
    next = EventControlNextForm()
    control = {'previous': previous, 'next': next}

    events = db.events(year, month)

    return render_template('event.html', year=year, month=month, control=control, events=events)


class EventControlPreviousForm(FlaskForm):
    submit = SubmitField('<')


class EventControlNextForm(FlaskForm):
    submit = SubmitField('>')




if __name__ == '__main__':
    app.run()
