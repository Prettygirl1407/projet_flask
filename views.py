from flask import Flask, render_template, request, redirect, Blueprint, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

views = Blueprint('views', __name__)

@views.route('/loginPage', methods = ['GET','POST'])
def loginPage():
    if request.method == 'GET':
        return render_template('loginPage.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Erreur, Veuillez ressayer', category='error')
            return redirect(url_for('views.loginPage'))
        
        login_user(user, remember=True)
        return redirect(url_for('main.profilePage'))

@views.route('/signUpPage', methods =['GET', 'POST'])
def signUpPage():
    if request.method == 'GET':
        return render_template('signUpPage.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Ce email exist deja', category='error')
            
        else:
            new_user = User(email=email, name=name, firstname=firstname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Votre compte a ete cree')
            
            return redirect(url_for('views.loginPage'))

@auth.route('/logoutPage')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



