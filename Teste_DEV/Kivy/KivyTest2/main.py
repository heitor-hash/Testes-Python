from kivy.uix.filechooser import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
import easygui as eg

class Home(Screen):
  def easy_read_file(self):
    path = eg.fileopenbox(
      title='Abra um arquivo',
      default='*.txt'
    )
    try:
      with open(path) as file:
        content = file.read()
      self.ids.File_content_label.text = content
    except:
      self.ids.File_content_label.text = 'LIGMA'

Builder.load_file("kiv.kv")

class MyApp(MDApp):
  def build(self):
    return Home()

if __name__=="__main__":
  MyApp().run()