# 🏠 API de Imóveis

## 📌 Sobre o projeto
Este projeto implementa uma **API RESTful de Imóveis** desenvolvida em **Python**, utilizando **TDD (Test-Driven Development)** para garantir qualidade e confiabilidade.  

A API permite criar, listar, atualizar, remover e filtrar imóveis.

---

## 🚀 Tecnologias utilizadas
- **Python 3.x**
- **Flask** (ou FastAPI, caso esteja usando)
- **Pytest** (testes automatizados)
- **SQLite/MySQL** (banco de dados)
- **Aiven** (para hospedagem do banco MySQL em nuvem, requisito da rubrica)
- **AWS** (para deploy da aplicação)

---

## ⚙️ Funcionalidades da API
- **Criar um imóvel** → `POST /imoveis`
- **Listar todos os imóveis** → `GET /imoveis`
- **Buscar imóvel por ID** → `GET /imoveis/{id}`
- **Filtrar imóveis por tipo** → `GET /imoveis/tipo/{tipo}`
- **Filtrar imóveis por cidade** → `GET /imoveis/cidade/{cidade}`
- **Atualizar imóvel existente** → `PUT /imoveis/{id}`
- **Remover imóvel** → `DELETE /imoveis/{id}`

Todos os endpoints retornam **códigos HTTP corretos**:
- `200 OK` → sucesso em consultas
- `201 Created` → criação bem-sucedida
- `204 No Content` → remoção sem conteúdo
- `404 Not Found` → recurso não encontrado
- `400 Bad Request` → erro de validação

---

## 📂 Estrutura do projeto

projeto-imoveis
│── api.py # Código principal da API
│ ├── rotas
│ └── modelos
│
│── test_api.py # Testes com pytest
│ └── testes das rotas e funções implementadas 
│
│── views.py
│└── 
│
│── requirements.txt # Dependências do projeto
│── README.md # Este arquivo
