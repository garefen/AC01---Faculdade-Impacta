from flask import Flask, make_response, request, render_template, redirect, send_from_directory
import os
import cmd_bd
import werkzeug

app = Flask(__name__)
@app.route("/")
def menu():
    return render_template("menu.html", mensagem = "")

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
        status = cmd_bd.Create_User(email,senha,nome)


        # Monta a resposta.
        mensagem = f"O Usuario {nome} com o email{email} foi criada com id {status['id_usuario']}."
        return render_template("menu.html", mensagem = mensagem)
    except Exception:
        mensagem = "Algo de errado não está certo."
        return render_template("menu.html", mensagem = mensagem)


if __name__ == '__main__':
    app.run()