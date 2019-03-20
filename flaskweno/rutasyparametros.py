from flask import Flask, redirect, url_for, render_template, request, session, flash
from models import db, User, Comment

import forms
from helper import date_format
from flask import g
import os
from flask_wtf.csrf import CsrfProtect
from flask import make_response
import json


from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect()





@app.route('/params')
def params():
    param = request.args.get('param1', 'este es el valor default en caso de que no se escriba nada en param1')
    return render_template("index.html", param = param )


@app.route('/client')
def client():
    list_name =["Eduardo", 'Isabel', 'Felipe', 'Nacho', 'Isidro']
    nombre = "Batman"
    return render_template("index.html", name = list_name, nombre = nombre)

@app.route('/form',  methods = ['GET', 'POST'])
def form():
    formulario = forms.doritos(request.form)
    if request.method == 'POST' and formulario.validate():
        print(formulario.username.data)
        print(formulario.email.data)
        print(formulario.comment.data)
    else:
        print ("Error en el formulario")
    return render_template("index.html", form = formulario)

@app.route('/create', methods =['GET', 'POST'])
def crearusuario():
    create_form = forms.doritos(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User( create_form.username.data,
                    create_form.password.data,
                    create_form.email.data)
        db.session.add(user)
        db.session.commit()
        success_message = 'Criamo o fila da puta'
        flash(success_message)
    return render_template("create.html", form = create_form)


@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['comments']:
        return redirect (url_for('login'))
    elif 'username' in session and request.endpoint in ['loginfunc', 'crearusuario']:
        return redirect(url_for('index'))

@app.route('/index')
def index():
    if 'username' in session:
        username = session['username']
        return f"Hola amigo: {username}"


@app.route('/comments', methods = ['GET','POST'])
def comments():
    comment_form = forms.comment(request.form)
    if request.method == 'POST' and comment_form.validate():
        user_id = session['user_id']
        comment = Comment(user_id = user_id, text = comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()
        success_message = 'Comentario Creado'
        flash(success_message)

    return render_template("comment.html", comment = comment_form)


@app.route('/reviews', methods =['GET'])
@app.route('/reviews/<int:page>', methods = ['GET'])
def reviews(page=1):
    per_page = 3
    comment = Comment.query.join(User).add_columns(User.username, Comment.text, Comment.create_date).paginate(page, per_page,False)
    return render_template("reviews.html", comment = comment, date_format = date_format)


@app.route('/login', methods=['GET', 'POST'])
def loginfunc():
    loginform = forms.LoginForm(request.form)
    if request.method == 'POST' and loginform.validate():
        username = loginform.username.data
        password = loginform.password.data
        user = User.query.filter_by(username = username).first()
        if user is not None and user.verify_password(password):
            session['username'] = username
            session['user_id'] = user.id
            success_message = "Wilkommen {}".format(username)
            flash(success_message)
            return redirect (url_for('index'))
        else:
            error_message = 'senha incorreta'
            flash(error_message)
    return render_template("login.html", login = loginform)

@app.route('/ajax-login', methods = ['POST'])
def ajax_login():
    print(request.form)
    username =  request.form['username']
    response = {'status':200, 'username': username, 'id':1 }
    return json.dumps(response)


@app.route('/cookie')
def cookiefunc():
    cook = 'Cookie'
    response = make_response( render_template("cookies.html", cook = cook))
    response.set_cookie('nombre_de_la_cookie', 'valor_de_la_galleta')
    return response


@app.route('/galleta')
def galleta():
    valor_galleta = request.cookies.get('nombre_de_la_cookie')
    return "{}".format(valor_galleta)


@app.route('/setups', methods=['GET', 'POST'])
def prebidpostbid():
    setup = forms.PrebidOrPostbid(request.form)
    if request.method == 'POST' and setup.validate():
        print(setup.setup.data)
    return render_template("setups.html", setup = setup)




'''


@app.route('/prueba')
def prueba():
    print("que deje que decidan")
    return f"antes y después! {g.test}"

@app.after_request
def after_request(response):
    print("en contra de su VOLUNTAD")
    return response
'''
if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port = 8000)
