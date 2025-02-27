import tkinter as tk
from tkinter import ttk
import dataHandler
import tkWidgets

texto_coletado:str

def OpenAndRead(nome_do_arquivo:str):
    global texto_coletado
    with open(nome_do_arquivo, 'r') as file:
        texto_coletado = file.read()
        file.close()
    texto_do_arquivo.delete(0.0, tk.END)
    texto_do_arquivo.insert(index=0.0, chars=texto_coletado)
    

def coletarTexto():
    try:
        n:str = nome_arquivo.get()
        OpenAndRead(n)
        Label_coletar_arquivo_resposta.config(text=f"Arquivo: '{n}' aberto com sucesso!")
    except:
        Label_coletar_arquivo_resposta.config(text=f"Arquivo: '{n}' não pode ser aberto ou não existe")
        
        
def TextToFile():
    global texto_coletado
    with open(entrada_nome_do_arquivo_para_salvar.get(), 'w') as file:
        file.write(texto_do_arquivo.get(index1=0.0, index2=tk.END))
        file.close()

root = tk.Tk()
root.geometry('500x400')
root.title("Teste de subArquivos")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text='File')
tabControl.add(tab2, text='Texto')
tabControl.add(tab3, text='Salvar')
tabControl.add(tab4, text='INDEV')

tabControl.pack(expand=1, # faz com que o tab ocupe o root todo
                fill='both') # em que eixo é prenxido, x, y, ambos ou nenhum

ttk.Label(tab1, text="Selecione um arquivo").pack()
ttk.Label(tab2, text="Texto do arquivo").pack()
ttk.Label(tab3, text="Digite o nome do arquivo para salvar").pack()
ttk.Label(tab4, text="EXCEL TEST").pack()

# TAB 1

nome_arquivo = tk.Entry(tab1, width=40)
nome_arquivo.pack()

botao_coletar_arquivo = tk.Button(tab1, text='Coletar', command=coletarTexto)
botao_coletar_arquivo.pack()

Label_coletar_arquivo_resposta = tk.Label(tab1, text="")
Label_coletar_arquivo_resposta.pack()

# TAB 2

texto_do_arquivo = tk.Text(tab2, width=60, height=5)
texto_do_arquivo.pack()

# TAB 3

entrada_nome_do_arquivo_para_salvar = tk.Entry(tab3, width=20)
entrada_nome_do_arquivo_para_salvar.pack()

botao_salvar_arquivo = tk.Button(tab3, text='Salvar', command=TextToFile)
botao_salvar_arquivo.pack()

# TAB 4

tab4_entries_list_keys = []
tab4_entries_list_values = []

dicio = {}
def EXCEL_read_to_dict():
    global dicio, tab4_entries_list_keys, tab4_entries_list_values
    path = dataHandler.easy_xl_file_selector()
    wb = dataHandler.open_workbook(path)
    dicio = dataHandler.worksheet_to_dict(wb=wb, sheet='dicio')
    wb.close()
    lista = []
    tab4_entries_list_keys = []
    tab4_entries_list_values = []
    i = 0
    for key, value in dicio.items():
        lista.append(key)
        lista.append(value)
        
        
        f, k, v = tkWidgets.entries_key_to_value(key, value)
        f.master = tab4_canva
        f.pack(in_=tab4_canva)
        
        tab4_entries_list_keys.append(k)
        tab4_entries_list_values.append(v)
    print(f"LISTA: {tab4_entries_list_keys}")

def EXCEL_add_kw_entry():
    global tab4_entries_list_keys, tab4_entries_list_values, tab4_frame_for_canvas
    
    f, k, v = tkWidgets.entries_key_to_value('', '')
    f.master = tab4_canva
    f.pack(in_=tab4_canva)
    
    tab4_entries_list_keys.append(k)
    tab4_entries_list_values.append(v)


def EXCEL_dict_to_xlsx():
    global tab4_entries_list_values, tab4_entries_list_keys
    path = dataHandler.easy_xl_save_file()
    wb = dataHandler.new_workbook(path)
    i = 0
    dicio_to_write = {}
    for key, value in zip(tab4_entries_list_keys, tab4_entries_list_values):
        dicio_to_write[key.get()] = value.get()
        
    print("DICIONARIO", dicio_to_write)
    dataHandler.dict_to_worksheet(wb=wb, sheet='dicio', dictionary=dicio_to_write, filename=path)
    wb.close()

    

tab4_button_read_xl_dados = tk.Button(tab4, text='READ', command=EXCEL_read_to_dict)
tab4_button_read_xl_dados.pack()

# Entries para colocar dados em forma de dicionário
# Create a canvas

tab4_frame_for_canvas, tab4_canva = tkWidgets.canvas_xy_vscroll(tab4)
tab4_frame_for_canvas.pack()

tab4_button_write_xl_dados = tk.Button(tab4, text='WRITE', command=EXCEL_dict_to_xlsx)
tab4_button_write_xl_dados.pack()

tab4_button_add_kw_entry = tk.Button(tab4, text="ADD", command=EXCEL_add_kw_entry)
tab4_button_add_kw_entry.pack()

root.mainloop()
