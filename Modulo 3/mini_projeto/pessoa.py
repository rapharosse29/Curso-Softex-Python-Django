class Pessoa:
    def __init__(self, nome: str, idade: int):
        # Chama os setters para garantir a validação já na inicialização
        self.nome = nome  
        self.idade = idade

    # --- GETTER PARA 'NOME' (já estava no seu código) ---
    @property
    def nome(self):
        """Método getter para obter o nome."""
        return self._nome

    # --- SETTER PARA 'NOME' ---
    @nome.setter  # O nome do decorator deve ser o mesmo nome do @property (nome)
    def nome(self, novo_nome: str):
        """Método setter para definir o nome, com validação."""
        if isinstance(novo_nome, str) and len(novo_nome.strip()) > 1:
            self._nome = novo_nome.strip().title() # Atribui o novo valor ao atributo privado
        else:
            print(f"Erro: O nome '{novo_nome}' é inválido. Deve ser um texto.")

    # --- GETTER PARA 'IDADE' ---
    @property
    def idade(self):
        """Método getter para obter a idade."""
        return self._idade

    # --- SETTER PARA 'IDADE' ---
    @idade.setter  # O nome do decorator deve ser o mesmo nome do @property (idade)
    def idade(self, nova_idade: int):
        """Método setter para definir a idade, com validação."""
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self._idade = nova_idade # Atribui o novo valor ao atributo privado
        else:
            print(f"Erro: A idade '{nova_idade}' é inválida. Deve ser um número inteiro não negativo.")

# --- Testando a Classe ---
print("--- 1. Criação e Getters ---")
p = Pessoa("maria silva", 25)
print(f"Nome: {p.nome}")
print(f"Idade: {p.idade}")

print("\n--- 2. Setters com Valores Válidos ---")
# O Python chama o @nome.setter
p.nome = "joão pereira"
# O Python chama o @idade.setter
p.idade = 40 
print(f"Novo Nome: {p.nome}") 
print(f"Nova Idade: {p.idade}")

print("\n--- 3. Setters com Validação (Erros) ---")
# Chamando o @nome.setter com valor inválido
p.nome = 123
# Chamando o @idade.setter com valor inválido
p.idade = -5

print(f"Nome (não mudou): {p.nome}") 
print(f"Idade (não mudou): {p.idade}") 