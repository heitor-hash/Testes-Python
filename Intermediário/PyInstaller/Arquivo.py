import sys

mod:list = sys.modules.keys()


modules_to_exclude = ['abc','builtins']
modules_to_exclude = list(sys.modules.keys())

for module in modules_to_exclude:
    if module in sys.modules:
        del sys.modules[module]
  
diff = sys.modules

# for module in modules_to_exclude:
#   try:
#     if diff[module] != '':
#       pass
#   except:
#     print("Modulo deletado")

for module in modules_to_exclude:
  print(module)

a = input("Input: ")

print(sys.modules.keys())

print(f"PRINTE {a}")

input()