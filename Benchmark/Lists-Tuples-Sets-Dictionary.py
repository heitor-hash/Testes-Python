import time

global index
index = 1

print("O programa está rodando, mas adicionar itens em uma tupla demora pra carai")

global lista
lista:list = ['a']
def list_add_item(item):
    global lista
    lista.append(item)
    
global tupla
tupla:tuple = ('a',)
def tuple_add_item(item):
    global tupla
    tupla = tupla + (item,)

global sett
sett:set = {'a'}
def set_add_item(item):
    global sett
    sett.add(item)
    
global dicio
dicio:dict = {'a':'b'}
def dicio_add_item(item):
    global dicio, index
    dicio[index]=item
    index += 1


start_time = time.time()
for i in range(100000):
    list_add_item(i)
list_add_time = time.time() - start_time


start_time = time.time()
for i in range(100000):
    tuple_add_item(i)
tuple_add_time = time.time() - start_time


start_time = time.time()
for i in range(100000):
    set_add_item(i)
set_add_time = time.time() - start_time


start_time = time.time()
for i in range(100000):
    dicio_add_item(i)
dicio_add_time = time.time() - start_time



print(f"Tempo da lista = {list_add_time:.6f} segundos")
print(f"Tempo da tupla = {tuple_add_time:.6f} segundos")
print(f"Tempo do set = {set_add_time:.6f} segundos")
print(f"Tempo do dicio = {dicio_add_time:.6f} segundos")


input()
print()

start_time = time.time()
for i in range(1,100000):
    lista[i]
end_time = time.time() - start_time
print(f"lista : {end_time:.6f}")

start_time = time.time()
for i in range(1,100000):
    tupla[i]
end_time = time.time() - start_time
print(f"tupla : {end_time:.6f}")


start_time = time.time()
for i in range(1,100000):
    next(iter(sett))
end_time = time.time() - start_time
print(f"set : {end_time:.6f}")


start_time = time.time()
for i in range(1,100000):
    dicio[i]
end_time = time.time() - start_time
print(f"dicio : {end_time:.6f}")


