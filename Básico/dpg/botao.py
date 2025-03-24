import dearpygui.dearpygui as dpg


class Counter():
  button_presses = 0
  

def button_press():
  n = Counter.button_presses+1
  dpg.set_value('Texto', f"Você clicou o botão! {n} vez{(lambda a: "es" if a > 1 else '')(a=n)}")
  Counter.button_presses = n

# Criar o contexto do DearPyGui
dpg.create_context()


# Criar a janela principal
with dpg.window(label="Janela Principal", tag="main_window"):
  dpg.add_text("Clique o botão!", tag='Texto')
  dpg.add_button(label="Botão", callback=button_press)
  
  
# Configurar a viewport (janela da aplicação)
dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

# Definir a janela principal como a principal
dpg.set_primary_window("main_window", True)

# Iniciar o loop da interface
dpg.start_dearpygui()
dpg.destroy_context()
