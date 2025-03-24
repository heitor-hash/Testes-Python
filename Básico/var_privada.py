from contextlib import contextmanager
from contextlib import nullcontext

# exec permite executar codigo restrito, sem que qualquer
# outra parte do codigo possa enxerga-los

# exemplo 1 de 2

codigo = """
a = 10
b = 15
c = lambda: a+b
print(c())

a = 50
print(c())
"""

exec(codigo)

# exemplo 2 de 2

exec("""
try:
  a = int(input("Digite um numero inteiro: "))
except:
  print("Escreveu errado, vai ser o numero 3")
  a = 3

print(f"O dobro do número é: {a*2}")



     """)



# Variável temporária

@contextmanager
def variavel_temporaria(valor):
  yield valor
  # Cria a variável temporária
  # Aqui ela some automaticamente

with variavel_temporaria("Isso é temporário") as temp:
  print(temp)  # Funciona dentro do 'with'
  
try:
  print(temp)
except:
  pass


# outro exemplo sem ter que criar nada de mais é esse
input("...")

with nullcontext():
  d = 0
  roller = 0
  printador = []
  for i in range(1, 101):
    d += i
    printador.append(str(d))
    roller += 1
    if roller > 2:
      print(f"{printador[0]:<6}|{printador[1]:^6}|{printador[2]:^6}")
      printador = []
      roller = 0