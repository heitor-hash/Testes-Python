# Teste para criação e leitura de arquivos txt

# Função escreve texto:
def WriteTextToFile(text:str) -> None: # O text é tipo str e a função retorna nada
    with open('TesteFile.txt', mode='w') as file:
        file.write(text)
        file.close()

def ReadFile() -> str: # Função retorna str
    with open('TesteFile.txt') as file:
        text = file.read()
        file.close()
        return text

class GetOutOfLoop ( Exception ):
    pass

try:
    while True:
        print("Digite uma função")
        print("| Read | Write | Sair |")
        escolha = input()
        if escolha.lower() == "read":
            try:
                print("Texto do arquivo:")
                print("-----------------------------")
                print(ReadFile())
                print("-----------------------------")
            except FileNotFoundError:
                print("Arquivo não encontrado")
        elif escolha.lower() == "write":
            text = input("Digite o texto que o arquivo terá:\n")
            try:
                WriteTextToFile(text)
                print("Arquivo criado ou editado com sucesso")
            except PermissionError:
                print("Arquivo está aberto em algum programa")
        elif escolha.lower() == 'sair':
            print('Programa encerrado')
            raise GetOutOfLoop
        else:
            print('Não entendi, pode escrever denovo?')
            continue
except GetOutOfLoop:
    pass


input('Precione "enter" para sair do programa')