class Tabela():
  index = 1
  def __init__(self, name):
    self.id = Tabela.index
    self.name = name
    Tabela.index += 1

tabela = Tabela(name="Robson")


return_code = tabela.name