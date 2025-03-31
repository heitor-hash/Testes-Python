import dearpygui.dearpygui as dpg


# lista_de_celulas = []
class Tabela():
  
  def __init__(self, respostas_certas:list, respostas_possiveis:list ):
    self.respostas_certas = respostas_certas
    self.respostas_possiveis = respostas_possiveis
    
  def clear_item_theme(data, sender):
    dpg.bind_item_theme(item=sender, theme=None)
    
  def create_tabela(self) -> None:
    # global lista_de_celulas
    with dpg.group(parent="main_window"):
      with dpg.table(
        tag='Tabela',
        borders_innerH=True,
        borders_innerV=True,
        borders_outerH=True,
        borders_outerV=True,
        resizable=True,
        show=True,
        scrollY=True,
        row_background=True,
        header_row=False,
      ):
        # Adiciona colunas baseadas na primeira linha
        if self.respostas_certas:
          num_colunas = len(self.respostas_certas[0])
          for _ in range(num_colunas):
            dpg.add_table_column()

        row_index = 1
        with dpg.table_row(tag=f'row0'):
          dpg.add_text(default_value="Selecione a alternativa")
          dpg.add_text(default_value="Bem, Direito ou Obrigação")
          dpg.add_text(default_value="Ativo ou Passivo")
          dpg.bind_item_theme('row0', 'header')
        
        for row in self.respostas_certas:
          with dpg.table_row(tag=f'row{row_index}'):
            # Primeira célula (texto)
            dpg.add_text(row[0])
            # Células seguintes (combos)
            for col_index, valor in enumerate(row[1:]):
              combo_tag = f"cell{row_index}-{col_index}"
              a = Callable_Cell(r_certa=valor, ref=combo_tag)
              
              # DEBUG DEBUG
              i = False
              for r in self.respostas_possiveis[col_index]:
                if r == valor:
                  i = True
              if i == False:
                print(f"ERRO, RESPOSTA {valor} NÃO EXISTE")
              # lista_de_celulas.append(a)
              dpg.add_combo(
                items=self.respostas_possiveis[col_index],
                default_value='',
                tag=combo_tag,
                callback=self.clear_item_theme
              )
          row_index += 1
              
class Callable_Cell():
  instancias = []
  def __init__(self, r_certa, ref:str):
    self.r_certa = r_certa
    self.ref:str = ref
    Callable_Cell.instancias.append(self)
    
  def check_answear(self, count_c:int, count_e:int):
    print(f'{dpg.get_value(self.ref):<20}|{self.r_certa:>15}')
    res = dpg.get_value(self.ref)
    if res == self.r_certa:
      # with dpg.group(parent=self.ref):
      dpg.bind_item_theme(item=self.ref, theme='correct')
      return count_c + 1, count_e
    elif res == '' or None:
      return count_c, count_e
    else:
      # with dpg.group(parent=self.ref):
      dpg.bind_item_theme(item=self.ref, theme='wrong')
      return count_c, count_e+1

def verificar_respostas():
  respostas_certas = 0
  respostas_erradas = 0
  for celula in Callable_Cell.instancias:
    respostas_certas, respostas_erradas = celula.check_answear(respostas_certas, respostas_erradas)
  print(f"respostas_certas é {respostas_certas}")
  dpg.set_value(item='text_n_r_certas', value=f"Respostas certas: {respostas_certas}")
  dpg.set_value(item='text_n_w_certas', value=f"Respostas erradas: {respostas_erradas}")
  

tabela_principal = Tabela(
  respostas_certas=[
    # 1ª coluna é indice
    # 2 a 4 é respostas
    ['Caixa', "Bem", 'Ativo'],
    ['Estoque', 'Bem', 'Ativo'],
    ['Capital Social', 'Obrigação', 'Passivo'],
    ['Veículos', 'Bem', 'Ativo'],
  ],
  respostas_possiveis=
  [
    # respostas possiveis para a 1ª coluna
    ['','Bem', 'Direito', 'Obrigação'],
    # respostas possiveis para a 2ª coluna
    ['','Ativo', 'Passivo'],
  ]
)

dpg.create_context()

# Theme
with dpg.theme(tag='main_theme'):
  with dpg.theme_component():
    dpg.add_theme_color(dpg.mvThemeCol_Text, (255,255,255))
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (70,70,80))
    dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (40,40,40))
    dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (55,55,55))
    dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (200,200,200,100))
    dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (220,220,220,100))
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (90,90,90,200))

with dpg.theme(tag='wrong'):
  with dpg.theme_component():
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (200,0,0))

with dpg.theme(tag='correct'):
  with dpg.theme_component():
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0,200,0))

with dpg.theme(tag='header'):
  with dpg.theme_component():
    dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (20,20,20))
    dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (20,20,20))


with dpg.font_registry():
  default_font = dpg.add_font("C:\\Windows\\Fonts\\arial.ttf", 20)

with dpg.window(label="Janela Principal", tag="main_window"):
  dpg.bind_font(default_font)
  dpg.bind_theme('main_theme')

tabela_principal.create_tabela()



dpg.create_viewport(title='Tabela de Exercício', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

with dpg.group(parent='main_window'):
  dpg.add_button(label='Verificar', callback=verificar_respostas)
  dpg.add_text(default_value='Respostas certas: ', tag="text_n_r_certas")
  dpg.add_text(default_value='Respostas erradas: ', tag="text_n_w_certas")

dpg.set_primary_window("main_window", True)


dpg.start_dearpygui()
dpg.destroy_context()