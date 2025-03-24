import dearpygui.dearpygui as dpg


# Criar o contexto do DearPyGui
dpg.create_context()


# Criar a janela principal
with dpg.window(label="Janela Principal", tag="main_window"):
  dpg.add_text("Olá, DearPyGui!")
  
  
# Configurar a viewport (janela da aplicação)
dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

# Definir a janela principal como a principal
dpg.set_primary_window("main_window", True)

# Iniciar o loop da interface
dpg.start_dearpygui()
dpg.destroy_context()
