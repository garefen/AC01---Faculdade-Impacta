
import mysql.connector
from contextlib import closing
import bd_AC2, SMS
from multiprocessing import Process
import threading
import time
import secrets
import string
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
def row_to_dict(description, row):
    if row == None: return None
    dictionary = {}
    for item in range(0, len(row)):
        dictionary[description[item][0]] = row[item]
    return dictionary

def Connection_String():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "petshop"
    )
    return connection
def Deletar(id,codigo):
    with closing(Connection_String()) as con, closing(con.cursor()) as cur:
        cur.execute("Select STATUS,codigo_validacao from AC2 WHERE id_usuario = %s", [id])
        teste1 = row_to_dict(cur.description, cur.fetchone())
        if teste1['STATUS'] == 1:
            return
        if teste1['codigo_validacao'] == codigo:
            cur.execute("UPDATE AC2 SET codigo_validacao = 123 WHERE id_usuario = %s", [id])
            con.commit()

app = Flask(__name__)
app.secret_key = 'EstaChaveNaoDeveSer1234'

@app.before_request
def before_request():
    g.user = None
    if 'id_usuario' in session is not None:
        user = bd_AC2.Consultar(session['id_usuario'])
        g.user = user
        

@app.route('/cadastro', methods=['GET', 'POST'])
def Cadastrar():
    
    if request.method == 'POST':
        session.pop('id_usuario', None)
        try:
            segredo = string.digits
            codigo = ''.join(secrets.choice(segredo) for i in range(4)) 
            teste = bd_AC2.Cadastrar(request.form['nome_usuario'], request.form['senha_usuario'], request.form['telefone_usuario'],codigo)
            SMS.enviar_sms(request.form['telefone_usuario'], codigo)
            session['id_usuario'] = teste['id_usuario']
            threading.Timer(100.0, Deletar,args=(teste['id_usuario'],codigo)).start()
        #threading.Timer(30.0, Deletar(teste['id_usuario'])).start()
        #p1 = Process(target=Chama_Deletar(teste['id_usuario']))
        #p1.start()
            return redirect(url_for('profile'))
        except Exception:
            erro = "Usuario não Cadastrado"
            return render_template('profile.html', erro = erro)
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    if g.user['STATUS'] == 0:
        return redirect(url_for('autenticar'))

    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST', 'DELETE'])
def login():
    #var = str(request.method)
    if request.method == 'POST':
        check = bd_AC2.Login(request.form['nome_usuario'], request.form['senha_usuario'])
        if check is None:
            return redirect(url_for('login'))
        session['id_usuario'] = check['id_usuario']
        if check['STATUS'] == 0:
            return redirect(url_for('autenticar'))
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/logout')
def logout():
        session.pop('id_usuario', None)
        return redirect(url_for('login'))

@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    if not g.user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        if request.form['codigo_validacao'] == g.user['codigo_validacao']:
            bd_AC2.Atualizar(g.user['id_usuario'])
            return redirect(url_for('profile'))
        else:
            erro = "Codigo incorreto"
            return redirect(url_for('autenticar', erro = erro))

    return render_template('autenticar.html')

@app.route('/enviarcodigo', methods=['GET', 'POST'])
def reenviar():
    segredo = string.digits
    codigo = ''.join(secrets.choice(segredo) for i in range(4)) 
    bd_AC2.Reenviar(g.user['id_usuario'],codigo)
    SMS.enviar_sms(g.user['telefone_usuario'], codigo)
    threading.Timer(100.0, Deletar,args=(g.user['id_usuario'],codigo)).start()
    return redirect(url_for('autenticar'))

if __name__ == '__main__':
    app.run()

    