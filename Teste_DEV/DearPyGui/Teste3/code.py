import dearpygui.dearpygui as dpg

with open(path) as file:
  code = file.read()

if not dpg.does_item_exist(item="code_text"):
  with dpg.group(parent="main_window"):
    dpg.add_text(code, before='classbutton', tag="code_text")