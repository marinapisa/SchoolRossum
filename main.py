from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from Models.pessoa import Pessoa
from Models.usuario import Usuarios


app = Flask(__name__)
app.secret_key = "123456"
SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\Marina-PC\\Documents\\Python\\SchoolRossum\\Banco\\aplication.sqlite3'
db = SQLAlchemy(app)

lista = Pessoa.query.order_by(Pessoa.id)

@app.route('/')
def inicio():
    lista = Pessoa.query.order_by(Pessoa.id)
    return render_template('lista.html', titulo = 'Lista de Alunos', pessoas = lista)

@app.route('/novo')
def cadastro():
    if 'usuario_logado' not in session or session ['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('novo')))
    return render_template('novo.html', titulo = 'Cadastro de Alunos')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form ['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas = Pessoa.query.filter_by(nome=nome).first()
    if pessoas:
        flash('Pessoa já existente!')
        return redirect(url_for('lista'))
    
    nova_pessoa = Pessoa(nome=nome, idade=idade, altura=altura)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('lista'))

@app.route('/editar')
def editar():
    return render_template('editar.html', titulo = 'Editar Aluno')

@app.route('/login')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo = 'School Rossum', proximo=proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario=Usuarios.query.filter_by(nickname=request.form['usuario'])
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] == usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
        flash('Usuário e/ou senha inválidos!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash('Você foi desconectado!')
    return redirect(url_for('login'))

app.run(debug=True)