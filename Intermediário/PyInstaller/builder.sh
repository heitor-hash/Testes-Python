# O builder não ira funcionar por padrão, você precisa de ter o
# pyinstaller no python,

# para isso:
# 1 - abra o cmd
# 2 - digite: pip install pyinstaller
# pronto

# para usar o upx (reduz o tamanho do executavel)
# 1 - baixe o upx do github oficial
# 2 - coloque em uma pasta qualquer
# 3 - quando for usar coloque o caminho para a pasta


# Transformar em executável com PyInstaller
# --onefile: único executável
# --noconsole: remove o console, útil se seu programa tem interface
# --clean: limpa arquivos temporários
# --exclude-module: remove módulos desnecessários
# --upx-dir: usa UPX para compactar
# --optimize: otimiza o código minimo = -1 , maximo = 2
# --name: define nome do .exe


# alguns dos módulos excluidos nem são de fato excluidos

pyinstaller \
  --onefile \
  --clean \
  --exclude-module pytest \
  --exclude-module tests \
  --exclude-module setuptools \
  --exclude-module tkinter \
  --exclude-module builtins \
  --exclude-module abc \
  --exclude-module xml \
  --exclude-module random \
  --exclude-module debugpy \
  --exclude-module subprocess \
  --exclude-module stat \
  --exclude-module struct \
  --exclude-module codecs \
  --exclude-module shutil \
  --exclude-module glob \
  --exclude-module binascii \
  --exclude-module inspect \
  --exclude-module _weakref \
  --exclude-module weakref \
  --exclude-module time \
  --exclude-module marshal \
  --exclude-module zipimport \
  --exclude-module nt \
  --exclude-module ntpath \
  --upx-dir="c\upx" \
  --optimize="2" \
  --name="Python em executavel" \
  "Arquivo.py"

  # --exclude-module zipfile \