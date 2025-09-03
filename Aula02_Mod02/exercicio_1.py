
vendas = [
    ("Teclado", 50, 2),
    ("Mouse", 25.50, 4),
    ("Monitor", 300, 1),
    ("Fone", 45, 1),
    ("Webcam", 75.20, 2)
]

vendas_filtradas = []
produtos_unicos =  set()

for item, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_filtradas.append((item, valor, quantidade))

    produtos_unicos.add(item)

print(f"Vendas filtradas (Valor Total >= 100): {vendas_filtradas}\n\n")
print(f"Itens únicos: {produtos_unicos}")

