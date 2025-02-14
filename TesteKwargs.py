#teste para *args e **kwargs

# *args são uma lista de argumentos
# para declaralos precisa do '*'

def ImprimeArgumentos(*argumentos):
    index = 1
    for arg in argumentos: # para cada argumento dentro do "argumentos"
        print(f"|{index:>3}º| argumento é |{arg:>10}|") # precisa do f para ele reconhecer o {var}
        index += 1

# o {index} printa o numero index e o ':>3' faz o alinhamento:
# :>5 = '    1'
# :<5 = '1    '
# :^5 = '  1  '

ImprimeArgumentos(1, "python", 15.15)

# espaço:
print("\n")

# agora para usar kwargs (key word argument), tipo um dicionário:
# para declaralo precisa do '**'

def ImprimeKWArgumentos(**argumentos):
    for chave, valor in argumentos.items(): # 'argumentos' é um dicionário então tem que usar o '.items()' para extrair valores
        print(f"|{chave:<15}| : |{valor:>15}|") # você já sabe porque precisa do f no inicio

ImprimeKWArgumentos(Nome='Heitor', Sobrenome='Vieira', idade=18)

# espaço:
print('\n')

# agora para transformar argumentos de input em kwargs
# primeiro metodo:

var_chave = input("Digite uma Chave: ")
var_valor = input("Digite um Valor: ")

ImprimeKWArgumentos(**{var_chave:var_valor}) # o ** é necessário para ele saber que é um kwarg

# espaço
print('\n')

# segundo metodo:

var_chave = input("Digite uma Chave: ")
var_valor = input("Digite um Valor: ")

argumento_kw = {var_chave:var_valor}

ImprimeKWArgumentos(**argumento_kw) # o ** é necessário porque ele espera "var=valor" mas recebe apenas "var"


# o programa fecha automaticamente quando não tem mais nada para fazer
# então eu coloco um input vazio no final
# o programa só fecha quando receber o ultimo valor


input()
