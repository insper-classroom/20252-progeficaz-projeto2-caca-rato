
import pytest
from unittest.mock import patch, MagicMock
from api import app
@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("views.connect_db")  # Substituímos a função que conecta ao banco por um Mock
def test_get_imoveis(mock_connect_db, client):
    """Testa a rota /alunos sem acessar o banco de dados real."""

    # Criamos um Mock para a conexão e o cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    # Configuramos o Mock para retornar o cursor quando chamarmos conn.cursor()
    mock_conn.cursor.return_value = mock_cursor

    # Simulamos o retorno do banco de dados
    mock_cursor.fetchall.return_value = [
        (1, 'Nicole Common', 'Travessa', 'Lake Danielle', 'Judymouth', 85184, 'casa em condominio', 488423.52, '2017-07-29'),
        (2,'Price Prairie', 'Travessa','Lake Danielle', 'Judymouth', 85184, 'apartamento', 488423.52, '2017-07-30')
    ]
    
    # Substituímos a função `connect_db` para retornar nosso Mock em vez de uma conexão real
    mock_connect_db.return_value = mock_conn
    
    # Fazemos a requisição para a API
    response = client.get("/imoveis")

    # Verificamos se o código de status da resposta é 200 (OK)
    assert response.status_code == 200

    # Verificamos se os dados retornados estão corretos
    expected_response = [
            {'id':1, 'logradouro':'Nicole Common', 'tipo_logradouro':'Travessa', 'bairro':'Lake Danielle', 'cidade':'Judymouth', 'cep':'85184', 'tipo':'casa em condominio', 'valor':488423.52, 'data_aquisicao':'2017-07-29'},
            {'id':2, 'logradouro':'Price Prairie', 'tipo_logradouro':'Travessa', 'bairro':'Lake Danielle', 'cidade':'Judymouth', 'cep':'85184', 'tipo':'apartamento', 'valor':488423.52, 'data_aquisicao':'2017-07-30'}
        ]
    assert response.get_json() == expected_response

@patch("views.connect_db")
def test_get_id(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        (1, 'Nicole Common', 'Travessa', 'Lake Danielle', 'Judymouth', 85184, 'casa em condominio', 488423.52, '2017-07-29'),
        (2,'Price Prairie', 'Travessa','Lake Danielle', 'Judymouth', 85184, 'apartamento', 488423.52, '2017-07-30')
    ]
    mock_connect_db.return_value = mock_conn
    id=1
    response = client.get(f"imoveis/{id}")
    assert response.status_code == 200
    expected_response = {
    'id': 1,
    'logradouro': 'Nicole Common',
    'tipo_logradouro': 'Travessa',
    'bairro': 'Lake Danielle',
    'cidade': 'Judymouth',
    'cep': '85184',
    'tipo': 'casa em condominio',
    'valor': 488423.52,
    'data_aquisicao': '2017-07-29'
}
    assert response.get_json() == expected_response

@patch("views.connect_db")
def test_novo_imovel(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect_db.return_value = mock_conn
    
    imovel = {
        'id':2,
        'logradouro':'teste',
        'tipo_logradouro':'teste_log',
        'bairro':'pirituba',
        'cidade':'sao paulo',
        'cep':'00000',
        'tipo':'casa',
        'valor':10000,
        'data_aquisicao':'2025-09-12',   
    }
    mock_cursor.fetchone.return_value = tuple(imovel.values())
    response = client.post("/imoveis", json=imovel)
    assert response.status_code == 201
    expected_response = imovel
    assert response.get_json() == expected_response

@patch("views.connect_db")
def test_att_imovel(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect_db.return_value = mock_conn
    
    imovel_antigo = (1, 'Nicole Common', 'Travessa', 'Lake Danielle', 'Judymouth', 85184, 'casa em condominio', 488423.52, '2017-07-29')
    imovel_att = (1, 'Nicole nova', 'T', 'lago novo', 'cidade nova', 11111, 'casa', 481223.52, '2025-09-15')
    
    mock_cursor.fetchone.side_effect = [imovel_antigo, imovel_att]
    
    atualizado = {
        "logradouro": "Nicole nova",
        "tipo_logradouro": "T",
        "bairro": "lago novo",
        "cidade": "cidade nova",
        "cep": "11111",
        "tipo": "casa",
        "valor": 481223.52,
        "data_aquisicao": "2025-09-15"
    }
    response = client.put("/imoveis/1", json=atualizado)
    
    assert response.status_code == 200
    expected_response = {
            'id': 1,
            'logradouro': 'Nicole nova',
            'tipo_logradouro': 'T',
            'bairro': 'lago novo',
            'cidade': 'cidade nova',
            'cep': '11111',
            'tipo': 'casa',
            'valor': 481223.52,
            'data_aquisicao': '2025-09-15'
        }
    assert response.get_json() == expected_response
    
@patch("views.connect_db")
def test_remove_imovel(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect_db.return_value = mock_conn
    
    mock_cursor.fetchall.return_value = [
        (1, 'Nicole Common', 'Travessa', 'Lake Danielle', 'Judymouth', 85184, 'casa em condominio', 488423.52, '2017-07-29'),
        (2,'Price Prairie', 'Travessa','Lake Danielle', 'Judymouth', 85184, 'apartamento', 488423.52, '2017-07-30')
    ]
    
    id=2
    response = client.delete(f"/imoveis/{id}")
    assert response.status_code == 200
    expected_response = {"message": f"Imóvel {id} removido com sucesso"}
    assert response.get_json() == expected_response
    
    
@patch("views.connect_db")
def test_list_tipo(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect_db.return_value = mock_conn
    
    mock_cursor.fetchall.return_value = [
    (1,'Nicole Common', 'Travessa', 'Lake Danielle', 'Judymouth', '85184', 'casa em condominio', 488423.52, '2017-07-29'),
    (2,'Price Prairie', 'Travessa', 'Colonton', 'North Garyville', '93354', 'casa em condominio', 260069.89, '2021-11-30')
]

    
    tipo = 'casa em condominio'
    
    response = client.get(f"/imoveis/tipo/{tipo}")
    assert response.status_code == 200
    expected_response = [
            {'id':1, 'logradouro':'Nicole Common', 'tipo_logradouro':'Travessa', 'bairro':'Lake Danielle', 'cidade':'Judymouth', 'cep':'85184', 'tipo':'casa em condominio', 'valor':488423.52, 'data_aquisicao':'2017-07-29'},
            {'id':2, 'logradouro':'Price Prairie', 'tipo_logradouro':'Travessa', 'bairro':'Colonton', 'cidade':'North Garyville', 'cep':'93354', 'tipo':'casa em condominio', 'valor':260069.89, 'data_aquisicao':'2021-11-30'}
        ]
    assert response.get_json() == expected_response
    
@patch("views.connect_db")
def test_list_cidade(mock_connect_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect_db.return_value = mock_conn
    
    mock_cursor.fetchall.return_value = [
        (1,'Nicole Common', 'Travessa', 'Lake Danielle', 'Judymouth', '85184', 'casa em condominio', 488423.52, '2017-07-29'),
        (2,'Price Prairie', 'Travessa', 'Colonton', 'Judymouth', '93354', 'casa em condominio', 260069.89, '2021-11-30'),
    ]
    
    cidade = 'Judymouth'
    
    response = client.get(f"/imoveis/cidade/{cidade}")
    assert response.status_code == 200
    expected_response = [
            {'id':1, 'logradouro':'Nicole Common', 'tipo_logradouro':'Travessa', 'bairro':'Lake Danielle', 'cidade':'Judymouth', 'cep':'85184', 'tipo':'casa em condominio', 'valor':488423.52, 'data_aquisicao':'2017-07-29'},
            {'id':2, 'logradouro':'Price Prairie', 'tipo_logradouro':'Travessa', 'bairro':'Colonton', 'cidade':'Judymouth', 'cep':'93354', 'tipo':'casa em condominio', 'valor':260069.89, 'data_aquisicao':'2021-11-30'},
        ]
    
    assert response.get_json() == expected_response
    

    