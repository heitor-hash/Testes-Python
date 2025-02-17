import time
# Classe é tipo um molde
# É tipo uma Super Variavel com variaveis e funções dentro


class BOOM( Exception ):
    pass
    
class Bomba:
    pavio:float
    def __init__(self, pavio):
        self.pavio = pavio
    
    def explosao(self):
        print("BOOOM!!!")
        raise BOOM


    
def main():
    try:
        # main loop
        while True:
            try:
                pav = float(input("Digite o tamanho do pavio em segundos: "))
            except:
                print("é para escrever em float\n")
                time.sleep(1.5)
                continue
            bomba = Bomba(pav)
            print(f"A bomba irá explodir em {pav:.2f} segundos")
            if pav > 3:
                time.sleep(pav - 2)
                print("A bomba irá explodir em 2 segundos")
                time.sleep(2)
                bomba.explosao()
            else:
                time.sleep(pav)
                bomba.explosao()
    except BOOM:
        time.sleep(0.5)
        print("O programa explodiu")

main()