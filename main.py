from flask import Flask, render_template, request, redirect, url_for
from package.controllers import livro_controller, usuario_controller, emprestimo_controller

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/livros")
def livros():
    return livro_controller.listar_livros()

@app.route("/usuarios")
def usuarios():
    return usuario_controller.listar_usuarios()

@app.route("/emprestimos")
def emprestimos():
    return emprestimo_controller.listar_emprestimos()

@app.route("/cadastrar_livro", methods=["POST"])
def cadastrar_livro():
    return livro_controller.cadastrar_livro(request)

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    return usuario_controller.cadastrar_usuario(request)

@app.route("/realizar_emprestimo", methods=["POST"])
def realizar_emprestimo():
    return emprestimo_controller.realizar_emprestimo(request)

@app.route("/devolver/<int:id>")
def devolver(id):
    return emprestimo_controller.devolver_livro(id)

if __name__ == "__main__":
    app.run(debug=True)
