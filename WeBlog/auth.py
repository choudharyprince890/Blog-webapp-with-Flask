from flask import Blueprint, render_template,redirect, url_for, request
auth = Blueprint("Auth", __name__)


@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    print(first_name,last_name,email,password,confirm_password)
    return render_template("signup.html")


@auth.route("/login", methods=['GET', 'POST'])
def Login():
    return render_template("login.html")

@auth.route("/logout")
def Logout():
    return redirect(url_for("views.home"))