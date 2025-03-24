# Teste de objetos

class Pessoas():
  lista_de_pessoas:list = []


class Pessoa():
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    Pessoas.lista_de_pessoas.append(self)
  
  def __del__(self):
    Pessoas.lista_de_pessoas.remove(self)
    
  def __str__(self) -> str:
    return self.nome
  


Pessoa("Joao", 20)
Pessoa("Robson", 35)

for a in Pessoas.lista_de_pessoas:
  print(a.nome)