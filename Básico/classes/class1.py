# Exemplo de classe como um dicionário

class Onibus():
  bancos = 30
  passageiros = ['José', 'Maria', 'Ricardo', 'Tadeu']
  combustivel = 80.05
  
  
dicio:dict = {
  'bancos':30,
  'passageiros':['José', 'Maria', 'Ricardo', 'Tadeu'],
  'combustivel':80.05
}

# Printa os passageiros do onibus
print(Onibus.passageiros)

print(dicio['passageiros'])