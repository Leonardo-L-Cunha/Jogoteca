from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

app.secret_key = 'pokemon123'
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Halo', 'Açao', 'Xbox')
jogo2 = Jogo('Mass Effect', 'RPG', 'Xbox 360')
jogo3 = Jogo('Gears 5', 'Açao', 'Xbox One')
    
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome,categoria,console)

    lista.append(jogo)
                 
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autencticar():
    if '1234' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'{session['usuario_logado'] } logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuario ou senha invalidos')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout com sucesso!')
    return redirect('/')    

app.run(host='localhost', port=8080, debug=True)