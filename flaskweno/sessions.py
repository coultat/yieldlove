from flask import Flask, render_template, request, session, redirect, url_for, flash
import forms
import os
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/formulario", methods = ['GET', 'POST'])
def sisyphus():
    formulario = forms.LoginForm(request.form)
    if request.method == 'POST' and formulario.validate():
        name = formulario.username.data
        success_message = f"bienvenido {name}"
        flash(success_message)
        session['username'] = formulario.username.data
        return render_template("logueado.html", login = formulario)
    return render_template("login.html", login = formulario)


@app.route("/login")
def login():
    if 'username' in session:
        username = session['username']
        print(username)
        return f"{username}"
    else:
        return "no te conoce ni el tato"

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('sisyphus'))


if __name__=='__main__':
    app.run (debug = True, port = 8000)
