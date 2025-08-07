from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db, login_manager
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

main_bp = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.is_admin:
                return redirect(url_for('main.admin_dashboard'))
            else:
                return redirect(url_for('main.user_dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('main.user_dashboard'))
    return render_template('admin_dashboard.html')

@main_bp.route('/dashboard')
@login_required
def user_dashboard():
    return render_template('user_dashboard.html')

@main_bp.route('/')
def index():
    return redirect(url_for('main.login'))
