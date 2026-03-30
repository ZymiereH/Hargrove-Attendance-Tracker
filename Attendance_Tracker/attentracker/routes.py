from flask import Flask, render_template, url_for, flash, redirect, request
from attentracker import app, db, bcrypt
from attentracker.forms import CheckoutForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required


names = [
    {
        'name': 'Zymiere Hargrove',
        'location': 'Room 46',
        'status': 'Present',
    },
    {
        'name': 'Ayden Parker',
        'location': 'Room 46',
        'status': 'Present',
    },
    {
        'name': 'Tahj Austion',
        'location': 'Room 46',
        'status': 'Present',
    },
    {
        'name': 'Doc Peterson',
        'location': 'Room 46',
        'status': 'Present',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', names=names)


@app.route("/admin")
def admin():
    return render_template('admin.html', title='Admin Page')


@app.route("/student")
def student():
    return render_template('student.html', title='Student Page')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form=form) 


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/checkout")
def checkout():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CheckoutForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data)
        db.session.add(user)
        db.session.commit()
        flash('Youve been checked out.', 'success')
        return redirect(url_for('checkout'))
    return render_template('checkout.html', title='Checkout', form=form)
