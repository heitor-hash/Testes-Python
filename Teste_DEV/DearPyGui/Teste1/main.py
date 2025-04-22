import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Janela Principal", tag="main_window"):
  dpg.add_text("Olá, DearPyGui!")

dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("main_window", True)

dpg.start_dearpygui()
dpg.destroy_context()
