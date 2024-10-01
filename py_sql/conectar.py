import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='',
        port='',
        user='',
        password='',
        database='infome aqui seu banco'
    )
    cursor = conexao.cursor()
    return conexao, cursor
