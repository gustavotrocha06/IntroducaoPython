from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados em memória para testes
produtos = [
    {"id": 1, "nome": "Teclado", "preco": 150.0},
    {"id": 2, "nome": "Mouse", "preco": 80.0}
]

# Rota Principal (GET)
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem": "API Flask a funcionar com sucesso!"})

# Rota para listar todos os produtos (GET)
@app.route('/produtos', methods=['GET'])
def get_produtos():
    return jsonify(produtos)

# TODO 1: Implementar uma rota GET para procurar um produto pelo ID
@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto_by_id(id):
    # Procura o produto com o ID correspondente
    produto = next((p for p in produtos if p["id"] == id), None)
    
    if produto:
        return jsonify(produto), 200
    
    # Retorna mensagem e status 404 quando o produto não existe
    return jsonify({"erro": "Produto não encontrado"}), 404

# TODO 2: Implementar uma rota POST para cadastrar um novo produto
@app.route('/produtos', methods=['POST'])
def add_produto():
    # Recupere os dados enviados no corpo da requisição usando request.get_json()
    # Adicione o novo produto à lista 'produtos'
    # Retorne o produto criado e o status code 201
    pass

if __name__ == '__main__':
    app.run(debug=True)