"""
Comércio Padaria - Desafio Python
x 1- O programa tem que rodar em loop infinito até ser parado pelo usuário.
x 2- Cliente pedir um tipo de pão (Frances, Doce, Forma, Australiano) 
x 3- Cada pão terá uma quantidade 
x 4- Valor do produto 
x 5- Pedir formas de pagamento (Dinheiro, Cartão, Pix)
x 6- Forma de entrega
x 7- Dados do Cliente (Em caso de delivery)
x 8- Valor do frete por bairro 
x 9- Nome do atendente 
x 10- Codigo de entrega
"""

def dados() -> dict:

## Carregar e retornar os dados de produtos, frete, funcionários

    return {
        "atendente": "Maria",
        "paes": {
            "frances": {"nome": "Pão Frances", "valor": 0.50, "quantidade": 15},
            "doce": {"nome": "Pão Doce", "valor": 5.00, "quantidade": 20},
            "forma": {"nome": "Pão de Forma", "valor": 5.99, "quantidade": 18}
        },
        "bairros": {
            "barroco": {"nome": "Barroco", "frete": 5.00},
            "sao jose": {"nome": "São José", "frete": 15.00}
        },
        "codigo_venda_base": 95875,
    }


def obter_dados_cliente() -> dict:

## Solicitar e retornar os dados do cliente

    nome = input("Informe seu nome: ")
    return {"nome": nome}


def solicitar_forma_pagamento() -> str:

## Solicitar e retornar a forma de pagamento escolhida
    while True:
        pagamento = input("Selecione a forma de pagamento (1- Dinheiro, 2- Cartão)")
        if pagamento == '1':
            return "Dinheiro"

        elif pagamento == '2':
            return "Cartão"
        
        else:
            print("Digite uma opção válida.")


def gerar_codigo_venda(codigo_base: int) -> int:

## Gera e retorna o código de venda
    return codigo_base + 1


def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float]:

## Calcula o valor do frete com base no bairro de entrega
    print("Bairros para entrega:")
    while True:
        for bairro in bairros_disponiveis.values():
            print(f"- {bairro["nome"]}")

        
        bairro_entrega_nome = input("Qual o bairro de entrega?").lower()

        bairro_encontrado = ""

        for chave, bairro in bairros_disponiveis.values():
            if bairro["nome"].lower() == bairro_entrega_nome:
                bairro_encontrado = chave
                break

        if not bairro_encontrado:
            print("Bairro fora da área de cobertura.")
        else:
            frete = bairros_disponiveis[bairro_encontrado]["frete"]
            return bairro_entrega_nome, frete
        
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

def atualizar_produto(estoque: dict) -> None:

## Permite ao atendente atualizar um produto existente.

    nome_produto = input("Digite o nome do produto para atualizar (Identificador): ").lower()
    if nome_produto not in estoque:
        print("Produto não cadastrado.")
        return

    print(f"Produto '{estoque[produto]}' selecionado. ")
    escolha = input("O que deseja atualizar?\n" \
    "1- Valor\n" \
    " 2- Quantidade)")

    try:
        if escolha == '1'
            novo_valor = float(input("Digite o novo valor do produto: "))
            if novo_valor > 0:
                estoque[nome_produto]["valor"] = novo_valor
                print(f"Valor atualizado para R$ {novo_valor:.2f}. ")
            else:
                print("Valor inválido.")
        elif escolha == "2"
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