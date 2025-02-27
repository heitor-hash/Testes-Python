import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x400')
root.title('Teste')

# Cria um container principal (Frame)
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Cria um Canvas dentro do container
canvas = tk.Canvas(main_frame)
canvas.pack(side='left', fill='both', expand=True)

# Cria uma Scrollbar vinculada ao Canvas
scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configura o Canvas para usar a Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Cria um Frame INTERNO para conter os widgets
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Adiciona widgets de exemplo ao Frame interno (roláveis)
for i in range(50):
    ttk.Label(inner_frame, text=f"Item {i + 1}").pack(pady=5)
    ttk.Button(inner_frame, text=f"Botão {i + 1}").pack()

# Atualiza a região de rolagem quando o tamanho do Frame interno mudar
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

inner_frame.bind("<Configure>", update_scrollregion)

root.mainloop()