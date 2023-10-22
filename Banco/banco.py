import sqlite3

print('testando entrada no arquivo')
try:
    conn = sqlite3.connect('aplication.sqlite3')
    print('Você acessou seu banco')
except Exception: 
    print('Você não esta conseguindo criar o arquivo Banco')

if conn is not None:
    print('Você estabilizou sua conexão')

    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE pessoa (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nome VARCHAR(15) NOT NULL, 
                   idade VARCHAR(40) NOT NULL, 
                   altura VARCHAR(20) NOT NULL  
                   );''')
    print('Sua tabela de pessoas foi cadastrada')
    cursor.execute('''CREATE TABLE Usuarios (
                   nome VARCHAR(20) NOT NULL, 
                   nickname VARCHAR(8) PRIMARY KEY NOT NULL, 
                   senha VARCHAR(100) NOT NULL  
                   );''')
    print('Sua tabela de Usuarios foi cadastrada')

    conn.commit()
    cursor.close()
    conn.close()