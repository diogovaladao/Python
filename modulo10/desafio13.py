from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
    'titulo': '72 Seasons',
    'estilo': 'Trash Metal'
},
{
    'titulo': 'Patience',
    'estilo': 'Hard Rock'
},
{
    'titulo': 'Paranoid',
    'estilo': 'Heavy Metal'
},
{
    'titulo': 'Wonderwall',
    'estilo': 'Brit pop'
},
{
    'titulo': 'On Top',
    'estilo': 'Indie Rock'
},
]

#rota padrão - GET http://localhost:5000
@app.route('/')
def obter_cancoes():
    return jsonify(cancoes)

#Get com ID  http://localhost:5000/cancao/1
@app.route('/cancao/<int:indice>', methods=['GET'])
def obter_cancao_por_id(indice):
    return jsonify(cancoes[indice], 200)

#criar nova cancao
@app.route('/cancao', methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(cancao, 200)

# Alterar cancao
@app.route('/cancao/<int:indice>', methods=['PUT'])
def alterar_cancao(indice):
    cancao_alterada = request.get_json()
    cancoes[indice].update(cancao_alterada)
    return jsonify(cancoes[indice], 200)

# Excluir cancao
@app.route('/cancao/<int:indice>', methods=['DELETE'])
def excluir_cancao(indice):
    try:
        if cancoes [indice] is not None:
            del cancoes[indice]
            return jsonify(f'Foi excluído a canção {cancoes[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a canção', 404)

app.run(port=5000,host='localhost', debug=True)