from flask import Flask,render_template,request, redirect

app = Flask(__name__)

class cadjogador:
    def __init__(self, nome, idade, posicao, experiencia, cidade, estado, dias, hora):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.experiencia = experiencia
        self.cidade = cidade
        self.estado = estado
        self.dias = dias
        self.hora = hora

lista = []

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/Criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    posicao = request.form['posicao']
    experiencia = request.form['experiencia']
    cidade = request.form['cidade']
    estado = request.form['estado']
    dias = request.form['dias']
    hora = request.form['hora']
    obj = cadjogador(nome, idade, posicao, experiencia, cidade, estado, dias, hora)
    lista.append(obj)
    return redirect('/Principal')

@app.route('/Cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo="Cadastre-se")

@app.route('/Principal')
def principal():
    return render_template('Principal.html', Titulo="Jogadores do clube", listajog=lista)

if __name__ == '__main__':
    app.run()