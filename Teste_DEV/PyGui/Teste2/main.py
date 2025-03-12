import dearpygui.dearpygui as dpg


lista_de_celulas = []
class Tabela():
  
  def __init__(self, respostas_certas:list, respostas_possiveis:list ):
    self.respostas_certas = respostas_certas
    self.respostas_possiveis = respostas_possiveis
    
  def create_tabela(self) -> None:
    with dpg.group(parent="main_window"):
      dpg.add_table(
        borders_innerH=True,
        borders_innerV=True,
        borders_outerH=True,
        borders_outerV=True,
        resizable=False,
        tag='Tabela',
        show=True
      )
      with dpg.group(parent='Tabela'):
        row_index = 0
        for row in self.respostas_certas:
          col_index = 0
          dpg.add_table_row(parent='Tabela', tag=f'row{row_index}')
          with dpg.group(parent=f'row{row_index}'):
            dpg.add_table_cell(parent=f'row{row_index}', label=row[0])
            for cell in row[1:]:
              a = Callable_Cell(r_certa=cell, ref=f"cell{row_index}-{col_index}")
              lista_de_celulas.append(a)
              dpg.add_table_cell(parent=f'row{row_index}', tag=f"cellholder{row_index}-{col_index}")
              with dpg.group(parent=f"cellholder{row_index}-{col_index}"):
                dpg.add_combo(items=self.respostas_possiveis[col_index],
                  tag=f"cell{row_index}-{col_index}")
              print(f'col : {col_index}')
              col_index += 1
          print(f'row : {row_index}')
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
    ['A', 'B', 'C'],
    ['Ligma','Figma', 'Rigma'],
    ['Ativo', 'Passivo']
  ]
)

dpg.create_context()

with dpg.window(label="Janela Principal", tag="main_window"):
  pass

tabela_principal.create_tabela()

dpg.create_viewport(title='Exemplo DearPyGui', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("main_window", True)


dpg.start_dearpygui()
dpg.destroy_context()