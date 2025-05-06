# Variável que armazena uma string
mensagem = "Bem-vindo ao estudo de variáveis e listas!"

# Lista que armazena várias strings
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Exibindo a mensagem
print(mensagem)

# Exibindo os itens da lista
print("Lista de frutas:")
for fruta in frutas:
    print(f"- {fruta}")

# Adicionando um novo item à lista
nova_fruta = "abacaxi"
frutas.append(nova_fruta)
print("\nApós adicionar uma nova fruta:")
print(frutas)

