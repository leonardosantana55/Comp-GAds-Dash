import os
import re

lista = os.scandir('C:/Users/leona/Downloadstest')

for li in lista:
    li = re.sub(r"(<DirEntry )|(')|(>)",'', str(li))
    print(li)
    os.remove(f'C:/Users/leona/Downloadstest/{li}')