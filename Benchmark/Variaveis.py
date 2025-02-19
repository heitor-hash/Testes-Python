import time



def met1(cont, mult):
    for vez in range(cont):
        resultado = (cont + vez) * mult
    return resultado
    
def met2(cont:int, mult:int):
    for vez in range(cont):
        resultado = (cont + vez) * mult
    return resultado
    
def met3(cont:int, mult:int) -> int:
    resultado:int
    for vez in range(cont):
        resultado:int = (cont + vez) * mult
    return resultado
    
start_time = time.time()
for _ in range(1000000):
    met1(10,10)
final_time = time.time() - start_time
print(f"Metodo 1 = {final_time:.6f}")

start_time = time.time()
for _ in range(1000000):
    met2(10,10)
final_time = time.time() - start_time
print(f"Metodo 2 = {final_time:.6f}")
    
start_time = time.time()
for _ in range(1000000):
    met3(10,10)
final_time = time.time() - start_time
print(f"Metodo 3 = {final_time:.6f}")