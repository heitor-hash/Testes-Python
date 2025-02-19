import tkinter as tk
from tkinter import ttk

global texto_coletado
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
root.title("Teste de Abas e Arquivo")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='File')
tabControl.add(tab2, text='Texto')
tabControl.add(tab3, text='Salvar')

tabControl.pack(expand=1, # faz com que o tab ocupe o root todo
                fill='both') # em que eixo é prenxido, x, y, ambos ou nenhum

ttk.Label(tab1, text="Selecione um arquivo").pack()
ttk.Label(tab2, text="Texto do arquivo").pack()
ttk.Label(tab3, text="Digite o nome do arquivo para salvar").pack()

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


root.mainloop()
