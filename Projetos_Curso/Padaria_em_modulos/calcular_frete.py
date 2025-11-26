def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float]:

## Calcula o valor do frete com base no bairro de entrega
    print("Bairros para entrega:")
    while True:
        for bairro in bairros_disponiveis.values():
            print(f"- {bairro["nome"]}")

        
        bairro_entrega_nome = input("Qual o bairro de entrega?").lower()

        bairro_encontrado = ""

        for chave, bairro in bairros_disponiveis.items():
            if bairro["nome"].lower() == bairro_entrega_nome:
                bairro_encontrado = chave
                break

        if not bairro_encontrado:
            print("Bairro fora da área de cobertura.")
        else:
            frete = bairros_disponiveis[bairro_encontrado]["frete"]
            return bairro_entrega_nome, frete