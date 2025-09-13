from flask import Flask, request
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import views

# Carrega as variáveis de ambiente do arquivo .cred (se disponível)
load_dotenv('.cred')

# Configurações para conexão com o banco de dados usando variáveis de ambiente
config = {
    'host': os.getenv('DB_HOST'),  # Obtém o host do banco de dados da variável de ambiente
    'user': os.getenv('DB_USER'),  # Obtém o usuário do banco de dados da variável de ambiente
    'password': os.getenv('DB_PASSWORD'),  # Obtém a senha do banco de dados da variável de ambiente
    'database': os.getenv('DB_NAME', 'imoveis'),  # Obtém o nome do banco de dados da variável de ambiente
    'port': int(os.getenv('DB_PORT')),  # Obtém a porta do banco de dados da variável de ambiente
    'ssl_ca': os.getenv('SSL_CA_PATH')  # Caminho para o certificado SSL
    
}

# Função para conectar ao banco de dados
def connect_db():
    """Estabelece a conexão com o banco de dados usando as configurações fornecidas."""
    try:
        # Tenta estabelecer a conexão com o banco de dados usando mysql-connector-python
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
    except Error as err:
        # Em caso de erro, imprime a mensagem de erro
        print(f"Erro: {err}")
        return None



app = Flask(__name__)


@app.route('/imoveis', methods=['GET'])
def get_imoveis():
    # conectar com a base de dados
    conn = connect_db()

    if conn is None:
        resp = {"erro": "Erro ao conectar ao banco de dados"}
        return resp, 500

    # se chegou até aqui, tenho uma conexão válida
    cursor = conn.cursor()

    sql = "SELECT * from imoveis"
    cursor.execute(sql)

    results = cursor.fetchall()
    if not results:
        resp = {"erro": "Nenhum aluno encontrado"}
        return resp, 404
    else:
        imoveis = []
        for imovel in results:
            
            imoveis.append({
                "id": imovel[0],
                "logradouro": imovel[1],
                "tipo_logradouro": imovel[2],
                "bairro": imovel[3],
                "cidade": imovel[4],
                "cep": str(imovel[5]),  
                "tipo": imovel[6],
                "valor": float(imovel[7]),
                "data_aquisicao": str(imovel[8])
            })

        resp = {"imoveis": imoveis}
    return resp, 200
    
@app.route('/imoveis/<int:id>', methods=['GET'])
def get_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    sql = f"SELECT id, logradouro,tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao FROM imoveis WHERE id = {id}"
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    imovel = {
                "id": result[0],
                "logradouro": result[1],
                "tipo_logradouro": result[2],
                "bairro": result[3],
                "cidade": result[4],
                "cep": str(result[5]),  
                "tipo": result[6],
                "valor": float(result[7]),
                "data_aquisicao": str(result[8])
            }
    return imovel, 200



if __name__ == '__main__':
    app.run(debug=True)