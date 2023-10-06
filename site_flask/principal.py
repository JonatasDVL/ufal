from flask import Flask, render_template

app = Flask(__name__) # iniciando o site

# criar a 1° página do site
# route -> caminho do site
# função -> o que voce quer exibir naquela página
# template -> utilize o render_template e coloque as pagunas html dentro de uma pagina chamada templates

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario) 

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) # debug=True faz com que o site fique atualizando toda hora