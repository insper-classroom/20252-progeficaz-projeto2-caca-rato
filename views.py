import os
import mysql.connector
import utils
from mysql.connector import Error
from dotenv import load_dotenv



# Carrega as variáveis de ambiente do arquivo .cred (se disponível)
load_dotenv('.cred')

# Configurações para conexão com o banco de dados usando variáveis de ambiente
config = {
    'host': os.getenv('DB_HOST'),  
    'user': os.getenv('DB_USER'),  
    'password': os.getenv('DB_PASSWORD'),  
    'database': os.getenv('DB_NAME', 'imoveis'),  
    'port': int(os.getenv('DB_PORT')),  
    'ssl_ca': os.getenv('SSL_CA_PATH')  
    
}

# Função para conectar ao banco de dados
def connect_db():
    """Estabelece a conexão com o banco de dados usando as configurações fornecidas."""
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
    except Error as err:
        print(f"Erro: {err}")
        return err

def get_imoveis():
    conn = connect_db()
    if conn is None:
        resp = {"erro": "Erro ao conectar ao banco de dados"}
        return resp, 500
    cursor = conn.cursor()

    sql = "SELECT * from imoveis"
    cursor.execute(sql)

    results = cursor.fetchall()
    if not results:
        resp = {"erro": "Nenhum imóvel encontrado"}
        return resp, 404
    imoveis = []
    for imovel in results:
        imoveis.append(utils.formata_imovel(imovel))
    resp = imoveis
    return resp, 200

def get_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imoveis WHERE id = %s", (id,))
    result = cursor.fetchall()[0]
    if not result:  
        return {"message": f"Imóvel com id {id} não encontrado"}, 404
    resp = utils.formata_imovel(result)
    return resp, 200
    
def novo_imovel(imovel):
    conn = connect_db()
    cursor = conn.cursor()
    # Cria novo imóvel
    sql = """
        INSERT INTO imoveis (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql, (
        imovel["logradouro"],
        imovel["tipo_logradouro"],
        imovel["bairro"],
        imovel["cidade"],
        imovel["cep"],
        imovel["tipo"],
        imovel["valor"],
        imovel["data_aquisicao"]
    ))
    conn.commit()
    new_id = cursor.lastrowid
    cursor.execute(
        "SELECT id, logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao FROM imoveis WHERE id = %s",
        (new_id,)   
    )
    result = cursor.fetchone()
    if not result:
        return {"message": f"Erro ao criar imóvel."}, 404
    resp = utils.formata_imovel(result)
    return resp, 201

def att_imovel(id, imovel):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM imoveis WHERE id = %s",
        (id,)
    )
    antigo = cursor.fetchone()
    if not antigo:
        return {"erro": "Imóvel não encontrado"}, 404

    sql = """
        UPDATE imoveis
        SET logradouro=%s, tipo_logradouro=%s, bairro=%s, cidade=%s,
            cep=%s, tipo=%s, valor=%s, data_aquisicao=%s
        WHERE id=%s
    """
    cursor.execute(sql, (
        imovel["logradouro"],
        imovel["tipo_logradouro"],
        imovel["bairro"],
        imovel["cidade"],
        imovel["cep"],
        imovel["tipo"],
        imovel["valor"],
        imovel["data_aquisicao"],
        id
    ))
    conn.commit()
    cursor.execute(
        "SELECT id, logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao FROM imoveis WHERE id = %s",
        (id,)
    )
    result = cursor.fetchone()
    resp = utils.formata_imovel(result)
    return resp, 200

def remove_imovel(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM imoveis WHERE id = %s", (id,))
    result = cursor.fetchone()

    if not result:
        return {"message": f"Imóvel {id} não encontrado"}, 404
    cursor.execute("DELETE FROM imoveis WHERE id = %s", (id,))
    conn.commit()
    return {"message": f"Imóvel {id} removido com sucesso"}, 200

def list_tipo(tipo):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM imoveis WHERE tipo = %s", (tipo,))

    results = cursor.fetchall()
    if not results:
        resp = {"erro": "Nenhum imóvel encontrado"}
        return resp, 404
    imoveis = []
    for imovel in results:
        imoveis.append(utils.formata_imovel(imovel))
    return imoveis, 200

def list_cidade(cidade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imoveis WHERE cidade = %s", (cidade,))
    results = cursor.fetchall()
    if not results:
        resp = {"erro": "Nenhum imóvel encontrado"}
        return resp, 404
    else:
        imoveis = []
        for imovel in results:
            imoveis.append(utils.formata_imovel(imovel))
    return imoveis, 200