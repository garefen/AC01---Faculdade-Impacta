
import bd_AC2, SMS
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

app = Flask(__name__)
app.secret_key = 'EstaChaveNaoDeveSer1234'

@app.before_request
def before_request():
    g.user = None
    if 'id_usuario' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/cadastro', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('id_usuario', None)
        try:
            segredo = string.digits
            codigo = ''.join(secrets.choice(segredo) for i in range(4)) 
            bd_AC2.Cadastrar(request.form['id_usuario'], request.form['nome_usuario'], request.form['senha_usuario'], request.form['telefone_usuario'],codigo)
            SMS.enviar_sms(request.form['telefone_usuario'], codigo)
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')
if __name__ == '__main__':
    app.run()