import sqlite3

conection = sqlite3.connect('banco.db')
cursor = conection.cursor()


cria_tabela = "CREATE TABLE IF NOT EXISTS   hoteis (hotel_id text PRIMARY KEY  ,\
    nome text , estrelas real , diaria real , cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha','alpha hotel',4.5,345.3 ,'Belo Horizonte')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

conection.commit()
conection.close()