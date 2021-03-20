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
'''
def fazer_login(login, senha):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT u.login, u.senha, u.nome FROM usuario u WHERE u.login = ? AND u.senha = ?", [login, senha])
        return row_to_dict(cur.description, cur.fetchone())
'''
def Create_User(email,senha,nome,telefone,codigo):
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "INSERT INTO tb_usuario(email_usuario, senha_usuario, nome_usuario, telefone, cod_seguranca, status) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(str(email), str(senha), str(nome), str(telefone), int(codigo), 0))
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
        cur.execute("SELECT id_usuario, nome_usuario, email_usuario, senha_usuario from tb_usuario WHERE id_usuario = %s", [id_usuario])
        return row_to_dict(cur.description, cur.fetchone())

def deletar_usuario(id_usuario):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("DELETE FROM tb_usuario WHERE id_usuario = %s", [id_usuario])
        con.commit()


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

def consultar_produto(id_produto):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_produto, nome_produto, tipo_produto, foto_produto, preco_compra_produto, preco_venda_produto,quantidade_produto from tb_produto WHERE id_produto = %s", [id_produto])
        return row_to_dict(cur.description, cur.fetchone())

def Update_Product(id_produto,nome,tipo,foto,preco_compra,preco_venda,quantidade):
    try:
        connection = Connection_String()
        cursor = connection.cursor()
        sql = "UPDATE tb_produto SET  nome_produto = %s,tipo_produto = %s,foto_produto =%s, preco_compra_produto = %s, preco_venda_produto = %s, quantidade_produto = %s where id_produto = %s"
        cursor.execute(sql,(str(nome), str(tipo),str(foto),str(preco_compra),str(preco_venda),str(quantidade), int(id_produto)))
        connection.commit()
        return {'id_produto': id_produto, 'nome': nome, 'tipo': tipo, 'foto': foto, 'preco_compra': preco_compra, 'preco_venda': preco_venda, 'quantidade' : quantidade}
    except Exception:
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def deletar_produto(id_produto):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("DELETE FROM tb_produto WHERE id_produto = %s", [id_produto])
        con.commit()