## Você tem o inventário de uma loja em duas listas de tuplas. Cada tupla representa um produto (nome_do_prouto, id).
"""
* estoque_principal: Produtos disponiveis na loja.
* estoque_online: Produtos disponíveis no site.

- Usando conjuntos, descubra e imprima:
1- Os produtos que estão disponiveis tanto na loja física quanto no site.
2- Os produtos que estão disponíveis apenas na loja física.
3- Os produtos que estão disponíveis apebas no site.

O que vai entrar:
estoque_principal = [("Camiseta", 101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]

"""

estoque_principal = [("Camiseta", 101), 
                     ("Calça", 102), 
                     ("Boné", 103), 
                     ("Tênis", 104)
]

estoque_online = [("Boné", 103), 
                  ("Camisa Polo", 105),
                  ("Calça", 102),
                  ("Chinelo", 106)
]

novo_estoque = set(estoque_principal)
novo_estoque_online = set(estoque_online)

loja_site = novo_estoque.intersection(novo_estoque_online)

loja = novo_estoque.difference(novo_estoque_online)

online = novo_estoque_online.difference(novo_estoque)

print(f"\n\nProdutos disponíveis na Loja e no Site: {loja_site}\n\n")
print(f"Produtos disponíveis apenas na loja: {loja}\n\n")
print(f"Produtos disponíveis apenas no site: {online}\n\n")
