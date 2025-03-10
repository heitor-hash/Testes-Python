from kivy.uix.filechooser import Screen
from kivymd.app import MDApp
from kivy.lang import Builder


class Home(Screen):
  pass

Builder.load_file("kiv.kv")

class MyApp(MDApp):
  def build(self):
    return Home()

if __name__=="__main__":
  MyApp().run()