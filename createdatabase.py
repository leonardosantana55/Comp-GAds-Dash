import mysql.connector

mydb = mysql.connector.connect(
    host="35.199.90.161",
    user='root',
    passwd='Ficalig4d0',
    database='comp-gads-dash'
)

mycursor = mydb.cursor()



mycursor.execute("CREATE TABLE intelbrasredes (palavrachave VARCHAR(255),\
                                                dominio VARCHAR(255), campanha VARCHAR(255), grupodeanuncios VARCHAR(255),\
                                                dia DATE,\
                                                parceladeimpressoes DECIMAL(10,2),\
                                                taxadesobreposicao DECIMAL(10,2),\
                                                taxaposicaosuperior DECIMAL(10,2),\
                                                taxapartesuperior DECIMAL(10,2),\
                                                taxada1aposicao DECIMAL(10,2),\
                                                parcelasuperacao DECIMAL(10,2))")

#for db in mycursor:
#    print(db)