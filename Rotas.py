from flask import Flask, make_response, request, render_template, redirect, send_from_directory
import os
import cmd_bd
import werkzeug

app = Flask(__name__)
@app.route("/")
def menu():
    return render_template("menu.html", mensagem = "")

@app.route("/usuario", methods=["GET"])
def listar_alunos_api():
    lista = cmd_bd.listar_usuarios()
    return render_template("lista_usuario.html", usuarios = lista)

@app.route("/usuario/novo", methods = ["GET"])
def carregar_usuario():
    usuario = {'id_usuario': 'novo', 'nome_usuario': '', 'email_usuario': '', 'senha_usuario': ''}
    return render_template("form_usuario.html", usuario = usuario)

@app.route('/usuario/novo', methods=['POST'])
def novo_usuario():
    try:
        email = request.form["email"]
        senha = request.form["senha"]
        nome = request.form["nome"]
        if len(email) < 1 or len(senha) < 1 or len(nome) < 1:
            raise Exception
        status = cmd_bd.Create_User(email,senha,nome)

        # Monta a resposta.
        mensagem = f"O Usuario {nome} com o email{email} foi criada com id {status['id_usuario']}."
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        mensagem = "Algo de errado não está certo."
        return render_template("menu.html", mensagem = mensagem)

@app.route("/produto/novo", methods = ["GET"])
def carregar_produto():
    produto = {'id_produto': 'novo', 'nome_produto': '', 'tipo_produto': '', 'foto_produto': '','preco_compra_produto': '', 'preco_venda_produto': '','quantidade_produto': '' }
    return render_template("form_produto.html", produto = produto)

@app.route('/produto/novo', methods=['POST'])
def novo_produto():
    try:
        nome = request.form["nome"]
        tipo = request.form["tipo"]
        foto = request.form["foto"]
        preco_compra = request.form["preco_compra"]
        preco_venda = request.form["preco_venda"]
        quantidade = request.form["quantidade"]
        if len(nome) < 1 or len(tipo) < 1 or len(preco_compra) < 1 or len(preco_venda) < 1 or len(quantidade) < 1:
            raise Exception
        status = cmd_bd.Create_Produto(nome,tipo,foto,preco_compra,preco_venda,quantidade)
        

        # Monta a resposta.
        mensagem = f"O produto {nome}  foi criado com id {status['id_produto']}."
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        mensagem = "Algo de errado não está certo."
        return render_template("menu.html", mensagem = mensagem)


if __name__ == '__main__':
    app.run()