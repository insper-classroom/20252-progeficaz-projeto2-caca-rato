# 🏠 Projeto 2 - Caça-Rato

## 📌 Sobre o projeto
Este projeto é uma API para gerenciamento de imóveis, desenvolvida em Python.  
O sistema permite realizar operações CRUD (Criar, Listar, Atualizar e Remover), além de filtros específicos, como por tipo de imóvel e cidade.  

Foram implementados testes automatizados com Pytest para garantir a confiabilidade das rotas. 

---

## 👥 Participantes
- Vinícius Oehlmann de Lima
- Erick Barbosa

---

## 🚀 Tecnologias utilizadas
- **Python 3.x**
- **Flask**
- **Pytest**
- **SQLite/MySQL**
- **Aiven**
- **AWS**

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

```plaintext
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
```

---

## 🌐 Deploy / Acesso

👉 [Acesse a API aqui](https://SEU-LINK-DA-API-AWS.com)