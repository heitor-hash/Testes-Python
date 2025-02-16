# programa com loop:
# começamos com as funções e as variaveis:

def Soma(numeros):
    soma: float = 0.0
    for num in numeros:
        soma += num
    return soma

def Mediana(numeros):
    numeros = list(numeros)
    numeros.sort()
    tamanho:int = len(numeros)
    medio = tamanho / 2
    if medio % 1 == 0:
        return (numeros[int(medio-1)] + numeros[int(medio)])/2
        
    else:
        print(str(numeros[int(medio-0.5)]) + "\n" + str(numeros[int(medio+0.5)]))
        return numeros[int(medio)]
        

# para sair do programa
class GetOutOfLoop( Exception ):
    pass


# main loop:

try:
    while True:

        # digite um numero ou operação:
        print("Digite um número ou função")
        print("Soma | Mediana | Sair")
        
        # recebedor de numero -> tuple
        nums = []
        recebido:str = ""
        is_func = None
        retorno:str = ""
        # loop para receber String:
        while is_func != True:
            recebido = input("Digite um número: ")
            try: # vê se dá para transformar em numero
                num = float(recebido)
                print(f"Valor digitado é : {recebido}")
                nums.append(num)
                print(nums)
            except: # Se não der para transformar em numero ve se é função
                if recebido.lower() == 'soma':
                    is_func = True
                    retorno = str(Soma(nums))
                elif recebido.lower() == 'mediana':
                    is_func = True
                    retorno = str(Mediana(nums))
                elif recebido.lower() == "sair":
                    print("Programa fechado")
                    raise GetOutOfLoop # quando ativo ele vai pro except GetOutOfLoop
                else: # Senão dá erro
                    is_func = True
                    print("Erro ao digitar valor, digite um numero ou função (Soma, Mediana)")
                    retorno = ""
                    
        if retorno == "":
            continue
        else:
            retorno = float(retorno)
            print(f"O valor da operação é \n---------------\n{retorno:>10.2f}\n---------------")
except GetOutOfLoop: #sai do programa
    pass

input("digite qualquer tecla para sair")