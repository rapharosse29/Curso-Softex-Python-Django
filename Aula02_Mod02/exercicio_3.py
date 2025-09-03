

acessos = [
    ("Pedro", "sucesso"),
    ("Ana", "falha"),
    ("Maria", "sucesso"),
    ("Pedro", "falha"),
    ("Ana", "falha"),
]

login_ok = set()
login_falha = set()

for usuario, status in acessos:
    if status == "sucesso":
        login_ok.add(usuario)
    elif status == "falha":
        login_falha.add(usuario)

somente_falha = login_falha.difference(login_ok)

print("Usuários com pelo menos um login bem-sucedido: ")
print(f"{login_ok}\n\n")