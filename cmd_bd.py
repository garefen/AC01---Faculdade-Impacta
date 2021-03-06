import mysql.connector

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
