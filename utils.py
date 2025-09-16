def formata_imovel(imovel):
    id_imovel = imovel[0]
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
                    "self": f"/imoveis/{id_imovel}",
                    "update": f"/imoveis/{id_imovel}",
                    "delete": f"/imoveis/{id_imovel}"
        }
    }
    return novo_imovel
