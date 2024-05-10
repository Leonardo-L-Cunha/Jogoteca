from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Halo', 'Mass Effect', 'Metal gear']
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run(host='localhost', port=8080)