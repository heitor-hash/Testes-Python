import dearpygui.dearpygui as dpg
import modpy as mod

def get_and_execute_code():
  data, path = mod.get_data_from_file()
  local_vars ={'path':path, 'return_code':''}
  exec(data, local_vars)
  return_code = local_vars["return_code"]
  if return_code != '' or None:
    print(return_code)


    
def run():
  dpg.create_context()

  with dpg.window(label="Janela Principal", tag="main_window"):
    dpg.add_text("Olá, DearPyGui!")
    dpg.add_button(label="Clique para pegar dados", callback=get_and_execute_code)
    
  dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
  dpg.setup_dearpygui()
  dpg.show_viewport()

  dpg.set_primary_window("main_window", True)

  dpg.start_dearpygui()
  dpg.destroy_context()

if __name__ == "__main__":
  run()