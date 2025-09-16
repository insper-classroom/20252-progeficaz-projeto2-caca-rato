from flask import Flask, request
import views


app = Flask(__name__)

@app.route('/imoveis', methods=['GET'])
def get_imoveis():
    resp = views.get_imoveis()
    return resp[0], resp[1]

@app.route('/imoveis/<int:id>', methods=['GET'])
def get_id(id):
    resp = views.get_id(id)
    return resp[0], resp[1]

@app.route('/imoveis', methods=['POST'])
def novo_imovel():
    imovel = request.get_json()
    resp = views.novo_imovel(imovel)
    return resp[0], resp[1]

@app.route('/imoveis/<int:id>', methods=['PUT'])
def att_imovel(id):
    imovel = request.get_json()
    resp = views.att_imovel(imovel)
    return resp[0], resp[1]

@app.route('/imoveis/<int:id>', methods=['DELETE'])
def remove_imovel(id):
    resp = views.remove_imovel(id)
    return resp[0], resp[1]

@app.route('/imoveis/tipo/<string:tipo>', methods=['GET'])
def list_tipo(tipo):
    resp = views.list_tipo(tipo)
    return resp[0], resp[1]

@app.route('/imoveis/cidade/<string:cidade>', methods=['GET'])
def list_cidade(cidade):
    resp = views.list_tipo(cidade)
    return resp[0], resp[1]



if __name__ == '__main__':
    app.run(debug=True)