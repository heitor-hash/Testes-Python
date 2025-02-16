#teste para *args e **kwargs

# Argumentos fixados são o padrão
# Para declaralos só precisa o escrever
def ImprimeArgFixado(argumento):
    print(argumento)



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

# Para o programa ter pausas adicione input
input("Precione enter para imprimir argumentos")

ImprimeArgumentos(1, "python", 15.15, "arg 4") # adicione mais argumentos e veja o que aconteçe
# resposta esperada:
# |  1º| argumento é |         1|
# |  2º| argumento é |    python|
# |  3º| argumento é |     15.15|
# |  4º| argumento é |     arg 4|

# espaço para pular      1 linha  : print()
print("\n") # para pular 2 linhas : print("\n")

# agora para usar kwargs (key word argument), tipo um dicionário:
# para declaralo precisa do '**'

def ImprimeKWArgumentos(**argumentos):
    for chave, valor in argumentos.items(): # 'argumentos' é um dicionário então tem que usar o '.items()' para extrair valores
        print(f"|{chave:<15}| : |{valor:>15}|") # você já sabe porque precisa do f no inicio

# Para o programa ter pausas adicione input
input("Precione enter para imprimir kwargumentos")

ImprimeKWArgumentos(Nome='Heitor', Sobrenome='Vieira', idade=18) # pode editar isso para ver o que aconteçe
# resposta esperada:
# |Nome           | : |         Heitor|
# |Sobrenome      | : |         Vieira|
# |idade          | : |             18|


print('\n')

# agora para transformar argumentos de input em kwargs
# primeiro metodo:
print("primeiro método:\n'(**{var_chave:var_valor})'")

var_chave = input("Digite uma Chave: ")
var_valor = input("Digite um Valor: ")

print()

ImprimeKWArgumentos(**{var_chave:var_valor}) # o ** é necessário para ele saber que é um kwarg

print()

# segundo metodo:
print("Segundo método:\n'argumento_kw = {var_chave:var_valor}'\n'ImprimeKWArgumentos(**argumento_kw)'")

var_chave = input("Digite uma Chave: ")
var_valor = input("Digite um Valor: ")

argumento_kw = {var_chave:var_valor}

ImprimeKWArgumentos(**argumento_kw) # o ** é necessário porque ele espera "var=valor" mas recebe apenas "var"


# Observações finais:
# *args é levemente mais lento que os Argumentos fixados
# **kwargs é levemente mais lento que o *args

# Então se você tem um codigo que roda umas milhares de vezes por segundo
# é preferivel você usar os argumentos fixados


# o programa fecha automaticamente quando não tem mais nada para fazer
# então eu coloco um input vazio no final
# o programa só fecha quando receber o ultimo valor


input()
