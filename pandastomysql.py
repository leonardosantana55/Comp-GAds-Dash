import pandas as pd
import os
import re


#encontra o arquivo certo na pasta downloads
file = None
li = os.scandir('C:/Users/leona/Downloads')
for x in li:
    if re.search("(redes-competicao)",str(x)): #aqui colocar o nome do relatório do cliente
         file = str(x)

#acerta o nome do arquivo
rep = ["<DirEntry ","'", ">"]
for y in rep:
    file = file.replace(y,"")
    #print(y)      
print(file)

df = pd.read_csv(f'C:/Users/leona/Downloads/{file}',skiprows=2)
df = df.rename(columns={"Pesquisar palavra-chave": "palavrachave",\
                        "Domínio do URL de visualização":"dominio",\
                        "Dia":"dia",\
                        "Parcela de impressões da pesquisa (Informações do leilão)":"parceladeimpressoes",\
                        "Taxa de sobreposição da pesquisa":"taxadesobreposicao",\
                        "Taxa de posição superior":"taxaposicaosuperior",\
                        "Taxa da parte superior da página":"taxapartesuperior",\
                        "Taxa da 1ª posição na página":"taxada1aposicao",\
                        "Campanha":"campanha",\
                        "Grupo de anúncios":"grupodeanuncios",\
                        "Parcela de superação da pesquisa":"parcelasuperacao"})

df = df.replace(",",".", regex=True)
df = df.replace("%","", regex=True)
df = df.replace("--",0, regex=True)
df = df.replace("< 10",0, regex=True)

from sqlalchemy import create_engine
engine = create_engine("mysql://guest:123456@35.199.90.161/comp-gads-dash?charset=utf8mb4")

df.to_sql('intelbrasredes', engine, if_exists='append', index=False)
pd.read_sql('intelbrasredes', engine)

