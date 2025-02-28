import tkinter as tk
from tkinter import ttk


def create_scrollbar_frame(root):
    # Cria um container principal (Frame)
    main_frame = tk.Frame(root)
    main_frame.pack(expand=1, fill='both')

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
    
    return main_frame, canvas, inner_frame


def data_to_label(frame, matrix:list):
    cols = 0
    for sublist in matrix:
        f = tk.Frame(frame, border=10)
        f.grid(column=cols, row=0)
        for item in sublist:
            tk.Label(f, text=item, border=2, bg="#999999").pack()
        cols += 1
        
        
        