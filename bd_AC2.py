import mysql.connector
from contextlib import closing

def row_to_dict(description, row):
    if row == None: return None
    dictionary = {}
    for item in range(0, len(row)):
        dictionary[description[item][0]] = row[item]
    return dictionary


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
        cur.execute("Insert into AC2 (nome_usuario, senha_usuario, telefone_usuario, codigo_validacao) Values (%s, %s, %s, %s) ", [str(nome), str(senha), str(tel), str(cod)])
        con.commit()
        id_usuario = cur.lastrowid
        return {'id_usuario': id_usuario}

def Consultar(usuario):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_usuario, nome_usuario, senha_usuario, telefone_usuario, codigo_validacao, STATUS FROM AC2  WHERE id_usuario = %s ", [usuario])
        return row_to_dict(cur.description, cur.fetchone())

def Atualizar(id_usuario):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE AC2 SET STATUS = 1 WHERE id_usuario = %s", [id_usuario])
        con.commit()
        return {'id_usuario': id_usuario}

def Deletar(id_usuario):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE AC2 SET codigo_validacao = NULL WHERE id_usuario = %s", [id_usuario])
        con.commit()

def Reenviar(id, codigo):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE AC2 SET codigo_validacao = %s WHERE id_usuario = %s", [codigo, id])
        con.commit()