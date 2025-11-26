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