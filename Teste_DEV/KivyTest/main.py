from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import easygui as easy
import time

Builder.load_file("kiv.kv") # O arquivo de widgets

# Esta é a classe base que servirá de container para os widgets.

class RootWidget(BoxLayout):    
    def open_file(self):
        path = easy.fileopenbox(
            default='*.txt',
            title='Abra um arquivo de texto'
        )
        try: # 'try' porque se falha o programa ía dar pau sem ele
            with open(path) as file:
                text = file.read()
            self.ids.meu_label.text = text
        except:
            pass
class MeuApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MeuApp().run()
    

    
    
    