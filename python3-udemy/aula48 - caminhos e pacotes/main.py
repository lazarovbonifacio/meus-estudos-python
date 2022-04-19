from pct1.mod1 import var1
from pct2.mod2 import var2

print(var1, var2)

# Todo arquivo de entrada tem {__name__} = '__main__'

# Como ele (Python) sabe que modulos importar e de onde importar?
import sys
print(sys.path)  # Onde o python procurar para importar modulos