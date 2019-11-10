# coding: utf-8
from flask import Blueprint, render_template, request, session, redirect, url_for
from ValidaUserDB import ValidaUser
from functools import wraps
import pymssql

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')


@bp_login.route("/")
def index():
    return render_template('Login.html')


@bp_login.route("/btnlogin", methods=['POST'])
def btnlogin():
    user = request.form.get('user')
    password = request.form.get('pass')

    ValidaUserBanco = ValidaUser()
    userBanco = ValidaUserBanco.validaUsuario(user, password)

    id = 0
    userNameDB = ""
    passwordDB = ""
    tipo = 0
    nome = ""

    for row in userBanco:
        id = row[0]
        userNameDB = row[1]
        passwordDB = row[2]
        grupo = row[3]
        nome = row[4]

    # Usuario correto
    if user == userNameDB and password == passwordDB:
        session.clear()
        session['id'] = id
        session['user'] = user
        session['grupo'] = grupo
        session['nome'] = nome
        return redirect(url_for('pedidos.index'))
    # user errado
    else:
        return redirect(url_for('login.index', userIncorrect=1))


@bp_login.route("/btnlogout", methods=['GET', 'POST'])
def btnlogout():
    session.pop('user', None)
    session.clear()
    return redirect(url_for('login.index'))


def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login.index', falhaSessao=1))
        else:
            return f(*args, **kwargs)

    return decorated_function
