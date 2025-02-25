import tkinter as tk


def entries_key40_to10_value60(key:str, value:str) -> tk.Frame | tk.Entry:
    small_frame = tk.Frame()
    key_entry = tk.Entry(small_frame, width=40)
    key_entry.pack(side='left')
    key_entry.insert('0', key)
    
    to_label = tk.Label(small_frame, width=10, text=':')
    to_label.pack(side='left')
    
    value_entry = tk.Entry(small_frame, width=60)
    value_entry.pack(side='right')
    value_entry.insert('0', value)
    
    return small_frame, key_entry, value_entry


def canvas_xy_vscroll(master) -> tk.Frame | tk.Canvas:
    frame = tk.Frame(master=master)
    
    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=1)
    
    scrollbar_y = tk.Scrollbar(frame, orient='vertical', command=canvas.yview_scroll, width=20)
    scrollbar_y.pack(side='right')
    
    canvas.configure(yscrollcommand=scrollbar_y.set)
    
    return frame, canvas