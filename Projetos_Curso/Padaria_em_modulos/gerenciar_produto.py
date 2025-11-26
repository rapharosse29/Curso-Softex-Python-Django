def cadastrar_produtos(estoque: dict) -> None:

## Permite ao atendente cadastrar novos produtos.
    nome_produto = input("Digite o nome do novo produto (Identificador): ").lower().strip()
    if nome_produto in estoque:
        print("ERROR!!! Produto já cadastrado com este identificador.")
        return
    
    try:
        nome_completo = input("Digite o nome completo do produto: ").strip()
        valor = float(input("Digite o valor do novo produto: "))
        quantidade = int(input("Digite a quantidade inicial do produto: "))

        if nome_produto and nome_completo and valor > 0 and quantidade > 0:
            estoque[nome_produto] = {"nome": nome_completo, "valor": valor, "quantidade": quantidade}
            print(f"Produto {nome_completo} cadastrado com sucesso!")

        else:
            print("Erro!!! Dados inválidos.")
    except ValueError:
        print("Entrada de dados inválida.")