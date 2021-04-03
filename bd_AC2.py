import mysql.connector
from contextlib import closing

def row_to_dict(description, row):
    if row is None: return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d

def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result

def Connection_String():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "petshop"
    )
    return connection

def Login(usuario, senha):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_usuario, nome_usuario, senha_usuario, telefone_usuario, codigo_validacao, STATUS FROM AC2  WHERE nome_usuario = %s AND senha_usuario = %s", [usuario, senha])
        return row_to_dict(cur.description, cur.fetchone())

def Cadastrar(nome, senha, tel, cod):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("Insert into AC2 (nome_usuario, senha_usuario, telefone_usuario, codigo_validacao) Values (%s, %s, %s, %s, %s) ", [nome, senha, tel, cod])
        return row_to_dict(cur.description, cur.fetchone())

def Consultar(usuario):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_usuario, nome_usuario, senha_usuario, telefone_usuario, codigo_validacao, STATUS FROM AC2  WHERE id_usuario = %s ", [usuario])
        return row_to_dict(cur.description, cur.fetchone())