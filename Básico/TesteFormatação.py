# Teste de formatação na função print do python
# Aqui vai ter algumas coisas para deixar o programa mais 'limpo'


# Print normal:
print("Nome : Heitor")

# Print com f-string:
nome = 'Heitor'
print(f"Nome : {nome}")

input("Precione enter\n")

# Formatação de print f-string

# Alinhado a direita em um espaco de 15 caracteres
print("Alinhamento a direita:")
print(f"Nome : |{nome:>15}|\n") 

# Alinhado a esquerda em um espaco de 15 caracteres
print("Alinhamento a esquerda:")
print(f"Nome : |{nome:<15}|\n")

# Alinhado no centro em um espaco de 15 caracteres
print("Alinhamento ao centro:")
print(f"Nome : |{nome:^15}|\n")

input("\nPrecione enter\n")


# Alinhamento com pontos
print("Alinhamento com '.' :")
print(f"Nome : |{nome:.^15}|\n")

print("Alinhamento com '-' :")
print(f"Nome : |{nome:-^15}|\n")

print("Alinhamento com '─' :") # alt + 452
print(f"Nome : |{nome:─^15}|\n")

print("Alinhamento com '○' :") # alt + 9
print(f"Nome : |{nome:○^15}|\n")