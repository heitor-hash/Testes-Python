import dearpygui.dearpygui as dpg
import easygui as egui

def get_data_from_file() -> str:
  path = egui.fileopenbox(
    title="Selecione codigo",
    default="*.py"
  )
  with open(path) as file:
    data = file.read()
  return data, path