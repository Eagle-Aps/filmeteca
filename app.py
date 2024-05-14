from flask import Flask, render_template

class Filme:
    def __init__(self, nome, genero, diretor):
        self.nome = nome
        self.genero = genero
        self.diretor = diretor

app = Flask(__name__)

@app.route('/home')
def home():
    
    filme1 = Filme('Pulp Fiction', 'Ação', 'Quentim Tarantino')
    filme2 = Filme('Batman 1989', 'Aventura', 'Tim Burton')
    filme3 = Filme('Jogador N° 1', 'Fantasia', 'Steven Spielberg')
    
    lista = [filme1, filme2, filme3]
    return render_template('lista.html', titulo='Filmes', filmes = lista)

@app.route('/newmovie')

def new_movie():
    
    return render_template('newmovie.html', titulo='Novo Filme')

app.run()