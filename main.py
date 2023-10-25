# 1414
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1414
app = Flask(__name__)
# uso o recurso do flask, condição para string de conexão com banco de dados, interna config e passo o caminho absoluto do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Marina-PC\\Documents\\Python\\SchoolRossum\\aplication.sqlite3'
# resurco do flask, condição de criptografia de senha
app.config['SECRET_KEY'] = 'rocknaveia'
db = SQLAlchemy(app)


from view import *
if __name__ == '__main__':
    app.run(debug=True)
