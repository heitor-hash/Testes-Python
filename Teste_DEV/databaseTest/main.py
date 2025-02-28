import tkinter as tk
from tkinter import ttk

import dataHandler as dd
import tkWidgets as ww


root = tk.Tk()
root.geometry('500x400')
root.title('Base de dados Excel')

tabControl = ttk.Notebook(root)

tabFile = tk.Frame(tabControl)

tabControl.add(tabFile, text='File')

tabControl.pack(expand=1, fill='both')

def EXCEL_to_data():
    global matriz_dadosXl
    path = dd.get_excel_path()
    wb = dd.open_workbook(path=path)
    sheet = dd.open_sheet(wb, "Sheet")
    # sheet = wb.active
    
    matriz_dadosXl = dd.excel_data_to_matrix(sheet)
    ww.data_to_label(xlRead_innerFrame, matriz_dadosXl)
    
    
    

tabFile_upperFrame = tk.Frame(tabFile, height=100)
tabFile_upperFrame.pack()

fileOpenButton = tk.Button(tabFile_upperFrame, text="Abrir", command=EXCEL_to_data)
fileOpenButton.pack()

fileWriteButton = tk.Button(tabFile_upperFrame, text="Salvar")

tabFile_lowerFrame = tk.Frame(tabFile, height=300)
tabFile_lowerFrame.pack()


xlRead_outerFrame, xlRead_canvas, xlRead_innerFrame = ww.create_scrollbar_frame(tabFile_lowerFrame)
xlRead_outerFrame.pack(expand=1, fill='both')

def update_scrollregion(event):
    xlRead_canvas.configure(scrollregion=xlRead_canvas.bbox("all"))

xlRead_innerFrame.bind("<Configure>", update_scrollregion)



root.mainloop()