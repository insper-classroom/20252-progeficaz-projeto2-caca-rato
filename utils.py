def formata_imovel(imovel):
    novo_imovel = {
                "id": imovel[0],
                "logradouro": imovel[1],
                "tipo_logradouro": imovel[2],
                "bairro": imovel[3],
                "cidade": imovel[4],
                "cep": str(imovel[5]),  
                "tipo": imovel[6],
                "valor": float(imovel[7]),
                "data_aquisicao": str(imovel[8])
            }
    return novo_imovel
