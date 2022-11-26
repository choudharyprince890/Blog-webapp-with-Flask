from flask import Blueprint, render_template,redirect, url_for, request, flash
from .import db 
from.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint("auth", __name__)




@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        print(first_name,last_name,email,password,confirm_password)

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Email is already in use ",category='error')
        elif password != confirm_password:
            flash("Password didn't match ",category='error')
        else: 
            #creating the user and saving to database
            new_user = User(email=email, first_name=first_name,last_name=last_name,password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("User created")
            return redirect(url_for("views.home"))

    return render_template("signup.html")


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        print(email,password)
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in",category="sucess")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("password is wrong ",category="error")
        else:
            flash("Email dows not exixt..", category="error")
    return render_template("login.html")



@auth.route("/logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for("views.home"))