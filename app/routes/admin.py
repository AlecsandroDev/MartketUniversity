from flask import Blueprint, render_template, redirect, url_for, jsonify
from flask import request,  session
from functools import wraps
from app.models.user import User, Anuncio, Reports, Administrator
import mysql.connector
from os import getenv as env
import json


admin_route = Blueprint('admin', __name__)


# Check if user is logon
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('admin.login')), 302
        return f(*args, **kwargs)
    return decorated_function


# Page Admin
@admin_route.route('/admin')
def login():
    return render_template("/admin/login.html"), 200

    
# Logon   
@admin_route.route('/admin-form', methods=["POST"])
def form_submit():
    username_form = request.form.get('username')
    password_form = request.form.get('password')
    
    administrator = Administrator.query.all()
    
    for user in administrator:
        if username_form == user.username and password_form == user.password:
            session['username'] = user.id
            return redirect(url_for("admin.dashboard")), 302
        else:
            return redirect(url_for("admin.login")), 302


# Remove session user
@admin_route.route('/admin/dashboard/logout', methods=["POST"])
def logout():
    session.pop('username', None)
    return redirect(url_for('admin.login'))


# Page Main Dashboard
@admin_route.route('/admin/dashboard')
@login_required
def dashboard():
    return render_template("/admin/dashboard.html"), 200


# Page Manage Products
@admin_route.route('/admin/dashboard/products')
@login_required
def products():
    return render_template("/admin/products.html"), 200


# Page Manage Users
@admin_route.route('/admin/dashboard/users')
@login_required
def users():
    return render_template("/admin/users.html"), 200


# Page Manage Reports
@admin_route.route('/admin/dashboard/reports')
@login_required
def reports():
    return render_template("/admin/reports.html"), 200


@admin_route.route('/users')
@login_required 
def list_users():
    usuarios = User.query.all()
    usuarios_list = [{
        'id': u.id,
        'nome': u.nome,
        'email': u.email,
        'telefone': u.telefone,
        'idade': u.idade,
        'cidade': u.cidade,
        'estado': u.estado
    } for u in usuarios]
    return jsonify(usuarios_list)


@admin_route.route('/products')
@login_required 
def list_products():
    anuncio = Anuncio.query.all()
    anuncios_list = [{
        'id': u.id,
        'titulo': u.titulo,
        'info': u.info,
        'preco': u.preco,
        'vendedor': u.vendedor,
    } for u in anuncio]
    return jsonify(anuncios_list), 200


@admin_route.route('/reports')
@login_required 
def list_reports():
    reportes = Reports.query.all()
    reportes_list = [{
        'id': u.id,
        'chamado': u.chamado,
        'usuario': u.usuario,
        'titulo': u.titulo,
        'info': u.info,
    } for u in reportes]
    return jsonify(reportes_list), 200


@admin_route.route('/admin/dashboard/users/manage_users/<int:id>')
@login_required
def manage_users(id):
    user = User.query.get_or_404(id)
    return render_template("admin/manage_users.html", user=user)


@admin_route.route('/update_user', methods=["POST"])
@login_required
def update_user():
    db_config = {
        "host": env('DB_HOST'),
        "user": env('DB_USER'),
        "password": env('DB_PASSWORD'),
        "database": env('DB_NAME')
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    id_form = request.form.get('id')
    username_form = request.form.get('nome')
    email_form = request.form.get('email')
    telefone_form = request.form.get('telefone')
    idade_form = request.form.get('idade')
    cidade_form = request.form.get('cidade')
    estado_form = request.form.get('estado')    

    cursor.execute("""
        UPDATE pessoas SET 
            nome=%s,            
            email=%s, 
            telefone=%s, 
            idade=%s, 
            cidade=%s, 
            estado=%s
        WHERE id=%s;
    """, (username_form, email_form, telefone_form, idade_form, cidade_form, estado_form, id_form))

    conn.commit()
    cursor.close()

    return redirect(url_for('admin.users'))