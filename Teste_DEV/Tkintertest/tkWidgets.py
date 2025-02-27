import tkinter as tk
from tkinter import ttk

def entries_key_to_value(key:str, value:str) -> tk.Frame | tk.Entry:
    small_frame = tk.Frame(height=10, width=100)
    small_frame.pack_propagate(0)
    key_entry = tk.Entry(small_frame, width=35)
    key_entry.pack(side='left')
    key_entry.insert('0', key)
    
    to_label = tk.Label(small_frame, width=5, text=':')
    to_label.pack(side='left')
    
    value_entry = tk.Entry(small_frame, width=40)
    value_entry.pack_propagate(False)
    value_entry.pack(side='left')
    value_entry.insert('0', value)
    
    return small_frame, key_entry, value_entry


def canvas_xy_vscroll(master) -> tk.Frame:
    frame = tk.Frame(master=master, height=50, width=500)
    frame.pack_propagate(False)
    
    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=True)
    
    scrollbar_y = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar_y.pack(side='right', fill='y')
    
    canvas.configure(yscrollcommand=scrollbar_y.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        
    
    inner_frame.bind("<Configure>", update_scrollregion)
    
    
    return frame, inner_frame