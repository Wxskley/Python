from flask import Flask, jsonify, request

app = Flask(__name__)


# Definindo uma rota para a API
@app.route("/api/exemplo", methods=["GET"])
def exemplo():
    # Dados fictícios de exemplo
    dados = {"nome": "João", "idade": 25, "profissao": "Engenheiro"}

    return jsonify(dados)


# Iniciando o servidor da API
if __name__ == "__main__":
    app.run()
