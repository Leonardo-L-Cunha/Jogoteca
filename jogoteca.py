from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Halo', 'Açao', 'Xbox')
jogo2 = Jogo('Mass Effect', 'RPG', 'Xbox 360')
jogo3 = Jogo('Gears 5', 'Açao', 'Xbox One')
    
lista = [jogo1, jogo2, jogo3]

@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome,categoria,console)

    lista.append(jogo)
                 
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(host='localhost', port=8080, debug=True)