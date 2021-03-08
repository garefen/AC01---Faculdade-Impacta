from flask import Flask, make_response, request, render_template, redirect, send_from_directory
import os
import cmd_bd
import werkzeug

app = Flask(__name__)
@app.route("/")
def menu():
    return render_template("menu.html", mensagem = "")

@app.route("/usuario", methods=["GET"])
def listar_alunos():
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

@app.route("/usuario/<int:id_usuario>", methods = ["GET"])
def carregar_alterar_usuario(id_usuario):
    try:
        usuario = cmd_bd.consultar_usuario(id_usuario)
        return render_template("form_usuario.html", usuario = usuario)
    except Exception:
        return render_template("menu.html", mensagem = f"Esse usuario não existe."), 404

@app.route("/usuario/<int:id_usuario>", methods = ["DELETE"])
def deletar_usuario(id_usuario):
    try:
        cmd_bd.deletar_usuario(id_usuario)
        mensagem = f"Usuario deletado"
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        return render_template("menu.html", mensagem = "Algo de errado não está certo"), 404


@app.route("/usuario/<int:id_usuario>", methods = ["POST"])
def editar_usuario(id_usuario):
    try:
        email = request.form["email"]
        senha = request.form["senha"]
        nome = request.form["nome"]
        if len(email) < 1 or len(senha) < 1 or len(nome) < 1:
            raise Exception
        cmd_bd.Update_User(id_usuario,email,senha,nome)
        mensagem = f"O Usuario {nome} com o email{email} foi alterado."
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        mensagem = "Algo de errado não está certo."
        return render_template("menu.html", mensagem = mensagem)

@app.route("/produto/novo", methods = ["GET"])
def carregar_produto():
    produto = {'id_produto': 'novo', 'nome_produto': '', 'tipo_produto': '', 'foto_produto': '','preco_compra_produto': '', 'preco_venda_produto': '','quantidade_produto': '' }
    return render_template("form_produto.html", produto = produto)

@app.route("/produto", methods=["GET"])
def listar_produto():
    lista = cmd_bd.listar_produtos()
    return render_template("lista_produtos.html", produtos = lista)

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
        mensagem = f"O produto {nome}  foi criado com id {status['id_produto']}."
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        mensagem = "Algo de errado não está certo."
        return render_template("menu.html", mensagem = mensagem)

@app.route("/produto/<int:id_produto>", methods = ["GET"])
def carregar_alterar_produto(id_produto):
    try:
        produto = cmd_bd.consultar_produto(id_produto)
        return render_template("form_produto.html", produto = produto)
    except Exception:
        return render_template("menu.html", mensagem = f"Esse produto não existe."), 404


@app.route("/produto/<int:id_produto>", methods = ["POST"])
def editar_produto(id_produto):
    try:
        nome = request.form["nome"]
        tipo = request.form["tipo"]
        foto = request.form["foto"]
        preco_compra = request.form["preco_compra"]
        preco_venda = request.form["preco_venda"]
        quantidade = request.form["quantidade"]
        if len(nome) < 1 or len(tipo) < 1 or len(preco_compra) < 1 or len(preco_venda) < 1 or len(quantidade) < 1:
            raise Exception
        cmd_bd.Update_Product(id_produto,nome,tipo,foto,preco_compra,preco_venda,quantidade)
        mensagem = f"O Produto {nome} foi alterado."
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        mensagem = "Algo de errado não está certo."
        return render_template("menu.html", mensagem = mensagem)

@app.route("/produto/<int:id_produto>", methods = ["DELETE"])
def deletar_produto(id_produto):
    try:
        cmd_bd.deletar_produto(id_produto)
        mensagem = f"Produto deletado"
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        return render_template("menu.html", mensagem = "Algo de errado não está certo"), 404

if __name__ == '__main__':
    app.run()