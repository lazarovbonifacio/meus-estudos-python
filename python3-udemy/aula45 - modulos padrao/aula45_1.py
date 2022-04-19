# modulos padrão: são arquivos .py (que contém codigo python) e servem para enpandir as funcionalidades
# padrão da linguagem. Veja todos os modulos padrão do Python em: https://docs.python.org/3/py-modindex.html

from sys import platform as so
print(so)

import random
print(random.randint(0,10))

# from random import *  # Má pratica
from random import random, randint

