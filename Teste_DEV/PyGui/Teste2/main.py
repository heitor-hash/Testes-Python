import dearpygui.dearpygui as dpg


lista_de_celulas = []
class Tabela():
  
  def __init__(self, respostas_certas:list, respostas_possiveis:list ):
    self.respostas_certas = respostas_certas
    self.respostas_possiveis = respostas_possiveis
    
  def create_tabela(self) -> None:
    global lista_de_celulas
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
        row_background=True
      ):
        # Adiciona colunas baseadas na primeira linha
        if self.respostas_certas:
          num_colunas = len(self.respostas_certas[0])
          for _ in range(num_colunas):
            dpg.add_table_column()

        row_index = 0
        for row in self.respostas_certas:
          with dpg.table_row(tag=f'row{row_index}'):
            # Primeira célula (texto)
            dpg.add_text(row[0])
            # Células seguintes (combos)
            for col_index, valor in enumerate(row[1:]):
              combo_tag = f"cell{row_index}-{col_index}"
              a = Callable_Cell(r_certa=valor, ref=combo_tag)
              lista_de_celulas.append(a)
              dpg.add_combo(
                items=self.respostas_possiveis[col_index],
                default_value='',
                tag=combo_tag
              )
          row_index += 1
              
class Callable_Cell():
  def __init__(self, r_certa, ref):
    self.resposta_certa = r_certa
    self.ref = ref
    
  def check_answear(self, count:int):
    if dpg.get_value(self.ref) == self.resposta_certa:
      return count + 1
    else:
      return count



tabela_principal = Tabela(
  respostas_certas=[
    ['Banco','A','Rigma','Ativo'],
    ['Dinheiro','A','Rigma','Ativo'],
    ["Conta de luz",'A','Rigma','Ativo']
  ],
  respostas_possiveis=
  [
    ['','A', 'B', 'C'],
    ['','Ligma','Figma', 'Rigma'],
    ['','Ativo', 'Passivo']
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
    dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (140,140,140,180))
    dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (170,170,170,210))

with dpg.theme(tag='wrong'):
  with dpg.theme_component():
    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (200,0,0))

with dpg.theme(tag='correct'):
  with dpg.theme_component():
    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0,200,0))


with dpg.font_registry():
  default_font = dpg.add_font("C:\\Windows\\Fonts\\arial.ttf", 20)

with dpg.window(label="Janela Principal", tag="main_window"):
  dpg.bind_font(default_font)
  dpg.bind_theme('main_theme')

tabela_principal.create_tabela()

dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("main_window", True)


dpg.start_dearpygui()
dpg.destroy_context()