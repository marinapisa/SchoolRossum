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
                   idade INTEGER NOT NULL, 
                   altura VARCHAR(20) NOT NULL  
                   );''')
    print('Sua tabela de pessoas foi cadastrada')
    cursor.execute('''CREATE TABLE usuarios (
                   nome VARCHAR(15) NOT NULL, 
                   nickname VARCHAR(30) PRIMARY KEY NOT NULL, 
                   senha VARCHAR(30) NOT NULL  
                   );''')
    print('Sua tabela de usuarios foi cadastrada')

    conn.commit()
    cursor.close()
    conn.close()