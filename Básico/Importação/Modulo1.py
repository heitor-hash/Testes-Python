class Aluno:
    nome:str
    idade:int
    def __str__(self): # Quando você finge que um Aluno é um str
        return(f"{self.nome}, {self.idade} ano(s)") # Ele retornao próprio nome e idade

    def aniversario(self):
        self.idade += 1 # Quando tem aniversário envelhece um ano
        
    def desintegrar(self):
        print("Adeus mundo cruel (◡︵◡)")
        del self 