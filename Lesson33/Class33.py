import psycopg2

HOST = 'localhost'
PORT = 5432
DATABASE = 'satesto'
USER = 'postgres'
PASSWORD = 'XX132Files'

conn = psycopg2.connect(host=HOST,port=PORT,database=DATABASE,user=USER,password=PASSWORD)

cursor = conn.cursor()






insert_query = """
    insert into customers(customerid, surname, firstname, city) values (
        '10000011','Frank', 'Sinatra','ny')"""
cursor.execute(insert_query)
conn.commit()
cursor.close()
conn.close()
