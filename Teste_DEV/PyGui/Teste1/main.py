import dearpygui.dearpygui as dpg



def create_window():
  if not dpg.does_item_exist("window_novo"):
    with dpg.window(label="Janela Nova", tag="window_novo"):
      dpg.add_checkbox(label="EXEMPLO")
    
def create_text():
  if not dpg.does_item_exist("text_main_window"):
    with dpg.group(parent="main_window"):
      dpg.add_text(default_value="Valor Padrão")

# Criar o contexto do DearPyGui
dpg.create_context()

with dpg.value_registry():
  dpg.add_string_value(tag="void_string", default_value="")

def button_command()-> None:
  command = dpg.get_value('radio_choice')
  if command == "Texto":
    create_text()
  elif command == "Window":
    create_window()

# Criar a janela principal
with dpg.window(label="Janela Principal", tag="main_window"):
  dpg.add_text("Olá, DearPyGui!")
  dpg.add_button(label="Adicionar: ", callback=button_command)
  dpg.add_radio_button(items=['Texto','Window'], horizontal=True, tag="radio_choice", default_value='Texto')


# Configurar a viewport (janela da aplicação)
dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

# Definir a janela principal como a principal
dpg.set_primary_window("main_window", True)

# Iniciar o loop da interface
dpg.start_dearpygui()
dpg.destroy_context()
