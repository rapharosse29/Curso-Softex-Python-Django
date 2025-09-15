def atualizar_produto(estoque: dict) -> None:

## Permite ao atendente atualizar um produto existente.

    nome_produto = input("Digite o nome do produto para atualizar (Identificador): ").lower()
    if nome_produto not in estoque:
        print("Produto não cadastrado.")
        return

    print(f"Produto '{estoque[nome_produto]}' selecionado. ")
    escolha = input("O que deseja atualizar?\n" \
    "1- Valor\n" \
    "2- Quantidade)")

    try:
        if escolha == '1':
            novo_valor = float(input("Digite o novo valor do produto: "))
            if novo_valor > 0:
                estoque[nome_produto]["valor"] = novo_valor
                print(f"Valor atualizado para R$ {novo_valor:.2f}.")
            else:
                print("Valor inválido.")
        elif escolha == '2':
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            
            if nova_quantidade > 0:
                estoque[nome_produto]["quantidade"] += nova_quantidade
                print(f"Quantidade atual de {estoque[nome_produto]["quantidade"]} itens.")
            else:
                print("Quantidade inválida! ")
        else:
            print("Erro!!! Opção inválida.")
    
    except ValueError:
        print("Erro!!! Entrada de dados inválida. Digite apenas números.")
