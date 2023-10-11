from flask import Flask, render_template, request, redirect, session, flash
from pessoa import Pessoa

pessoa1 = Pessoa('Rodrigo', 32, 1.87)
pessoa2 = Pessoa('Marina', 29, 1.69)
pessoa3 = Pessoa('André', 26, 1.80)
pessoa4 = Pessoa('Carlos', 55, 1.75)
pessoa5 = Pessoa('Elaine', 48, 1.82)

lista = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5 ]

app = Flask(__name__)
app.secret_key = "123456"

@app.route('/')
def inicio():
    return render_template('lista.html', titulo = 'Lista de Alunos', pessoas = lista)

@app.route('/novo')
def cadastro():
    return render_template('novo.html', titulo = 'Cadastro de Alunos')

@app.route('/editar')
def editar():
    return render_template('editar.html', titulo = 'Editar Aluno')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form ['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas = Pessoa(nome, idade, altura)
    
    lista.append(pessoas)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'School Rossum')

@app.route('/autenticar')
def autenticar():
    if '123456' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + "Você está logado")
    else:
        flash("Senha incorreta, tente novamente!")
        redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash('Você foi desconectado!')
    return redirect("/login")

app.run(debug=True)