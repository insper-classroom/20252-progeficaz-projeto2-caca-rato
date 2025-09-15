
import pytest
from unittest.mock import patch, MagicMock
from api import app
@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("api.connect_db")  # Substituímos a função que conecta ao banco por um Mock
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
    expected_response = {
        "imoveis": [
            {'id':1, 'logradouro':'Nicole Common', 'tipo_logradouro':'Travessa', 'bairro':'Lake Danielle', 'cidade':'Judymouth', 'cep':'85184', 'tipo':'casa em condominio', 'valor':488423.52, 'data_aquisicao':'2017-07-29'},
            {'id':2, 'logradouro':'Price Prairie', 'tipo_logradouro':'Travessa', 'bairro':'Lake Danielle', 'cidade':'Judymouth', 'cep':'85184', 'tipo':'apartamento', 'valor':488423.52, 'data_aquisicao':'2017-07-30'}
        ]
    }
    assert response.get_json() == expected_response

@patch("api.connect_db")
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

@patch("api.connect_db")
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
    response = client.post("/criar", json=imovel)
    assert response.status_code == 201
    expected_response = {
        "imoveis": [imovel]
    }
    assert response.get_json() == expected_response
