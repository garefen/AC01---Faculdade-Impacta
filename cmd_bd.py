import mysql.connector
from contextlib import closing

def Connection_String():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "petshop"
    )
    return connection


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


def Create_User(email,senha,nome):
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "INSERT INTO tb_usuario(email_usuario, senha_usuario, nome_usuario) VALUES(%s, %s, %s)"
        cursor.execute(sql,(str(email), str(senha), str(nome)))
        connection.commit()
        id_usuario = cursor.lastrowid
        return {'id_usuario': id_usuario, 'email': email, 'senha': senha, 'nome': nome}
    except Exception:
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def Update_User(id_usuario,email,senha,nome):
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "UPDATE tb_usuario SET  email_usuario = %s,senha_usuario = %s,nome_usuario =%s where id_usuario = %s"
        cursor.execute(sql,(str(email), str(senha),str(nome), int(id_usuario)))
        connection.commit()
        return {'id_usuario': id_usuario, 'email': email, 'senha': senha, 'nome': nome}
    except Exception:
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def listar_usuarios():
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "SELECT * from tb_usuario order by id_usuario"
        cursor.execute(sql,)
        rows = cursor.fetchall()
        user_list = rows_to_dict(cursor.description, rows)
        return user_list
    finally:
        cursor.close()
        connection.close()

def consultar_usuario(id_usuario):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_usuario, nome_usuario, email_usuario, senha_usuario WHERE id_usuario = %s", [id_usuario])
        return row_to_dict(cur.description, cur.fetchone())


def Create_Produto(nome,tipo,foto,preco_compra,preco_venda,quantidade):
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "INSERT INTO tb_produto(nome_produto, tipo_produto, foto_produto, preco_compra_produto, preco_venda_produto, quantidade_produto) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(str(nome), str(tipo), str(foto),str(preco_compra), str(preco_venda), str(quantidade)))
        connection.commit()
        id_produto = cursor.lastrowid
        return {'id_produto': id_produto, 'nome': nome, 'tipo': tipo, 'foto': foto, 'preco_compra': preco_compra, 'preco_venda': preco_venda, 'quantidade' : quantidade}
    except Exception:
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def listar_produtos():
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "SELECT * from tb_produto order by id_produto"
        cursor.execute(sql,)
        rows = cursor.fetchall()
        user_list = rows_to_dict(cursor.description, rows)
        return user_list
    finally:
        cursor.close()
        connection.close()