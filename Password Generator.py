import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Bem vindo ao gerador de senhas automático")
qtd_letras = int(input("Quantas letras você deseja em sua senha automática?\n "))
qtd_numeros = int(input("Quantos números você deseja em sua senha automática?\n "))
qtd_simbolos = int(input("Quantos símbolos você deseja em sua senha automática?\n "))
                   

senha_valores = []
for char in range(1, qtd_letras + 1):
  senha_valores.append(random.choice(letras))
for char in range(1, qtd_simbolos + 1):
  senha_valores += random.choice(simbolos)
for char in range(1, qtd_numeros + 1):
  senha_valores += random.choice(numeros)
print(senha_valores)
random.shuffle(senha_valores)
print(senha_valores)

senha = ""
for char in senha_valores:
  senha += char

print(f"Sua senha automática é: {senha}")
