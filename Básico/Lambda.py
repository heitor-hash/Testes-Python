# Lambda é uma pequena função anônima que pode ter no máximo 1 expressão
# Lambda argumento : expressão

# Em python lambda pode ser chamada como uma variavel:
VarFuncao = lambda a: a + 5 # varfunção recebe 1 argumento (a) e retorna (a + 5)

print(VarFuncao(20)) # resultado 25

# Lambda pode receber mais de um argumento:

VarSomador = lambda a, b, c: a + b + c

print(VarSomador(5,10,2)) # 5 + 10 + 2
# Resultado 17


# A parte mais complicada de entender é lambda dentro de uma função
# lambda pode ser chamada dentro de uma função que requer 1 argumento

def FuncaoSub(sub):
    return lambda num: num - sub

# variavel 'menos2' é uma referência a FuncaoSub
menos2 = FuncaoSub(2) # sub = 2

# depois chamamos menos2 para chamar a função
print(menos2(5)) # sub = 2, num = 5
# resultado = 3

# também podemos chamar a função em uma linha
# porém temos que usar 2 espaços para colocar argumentos
# o que pode ser difícil de entender
print(FuncaoSub(10)(5)) # sub = 10, num = 5
# resultado = -5