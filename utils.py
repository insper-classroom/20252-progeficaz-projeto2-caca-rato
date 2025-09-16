def formata_imovel(imovel):
    id_imovel = imovel[0]
    base_url = "http://127.0.0.1:5000/imoveis"  # ou use variável de ambiente se for em produção

    novo_imovel = {
        "id": id_imovel,
        "logradouro": imovel[1],
        "tipo_logradouro": imovel[2],
        "bairro": imovel[3],
        "cidade": imovel[4],
        "cep": str(imovel[5]),
        "tipo": imovel[6],
        "valor": float(imovel[7]),
        "data_aquisicao": str(imovel[8]),
        "links": {
            "self": {
                "href": f"{base_url}/{id_imovel}",
                "method": "GET"
            },
            "update": {
                "href": f"{base_url}/{id_imovel}",
                "method": "PUT"
            },
            "delete": {
                "href": f"{base_url}/{id_imovel}",
                "method": "DELETE"
            }
        }
    }
    return novo_imovel
