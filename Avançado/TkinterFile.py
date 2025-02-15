# Quase igual ao arquivo TesteTkinter.py só que com criação de arquivos

# importa o tkinter, a biblioteca para criar aplicativos
import tkinter as tk

# Começa o programa

root = tk.Tk()
root.title("Exemplo Tkinter")

# Tamanho da tela:
root.geometry('500x400')

# Função para o botão de fechar
def CloseWindow():
    root.destroy()

# Botão de fechar
CloseButton = tk.Button(root, text='Sair', command=CloseWindow)
CloseButton.place(x=5,y=5)

# Input para coletar texto
EntradaTexto = tk.Entry(root, width=50)
EntradaTexto.place(x=5,y=35)

# Botão para ler o texto
Texto_Coletado:str = 'Texto Exemplo'
def ColetarTexto():
    global Texto_Coletado
    Texto_Coletado = EntradaTexto.get()
    TextoUpdate()

ReadButton = tk.Button(root, text='Coletar Texto', command=ColetarTexto)
ReadButton.place(x=5,y=65)

# Mostra o texto coletado:
PrintTexto = tk.Text(root, height=2, width=50)
PrintTexto.place(x=5,y=95)
PrintTexto.insert(index=0.0, chars="Texto Exemplo")

def TextoUpdate():
    PrintTexto.delete(index1=0.0, index2=tk.END)
    PrintTexto.insert(index=0.0, chars=Texto_Coletado)
    
def TextToFile():
    with open(file='TkinterFile.txt', mode='w') as file: # w = write, substitui texto do arquivo
        file.write(Texto_Coletado)
        file.close()

TTFButton = tk.Button(root, text="Texto para arquivo TkinterFile.txt", command=TextToFile)
TTFButton.place(x=5,y=155)

# Roda o arquivo
root.mainloop()