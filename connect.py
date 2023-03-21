import psycopg2
from config import config

def connect():
    conn = None
    try:
        """A variavel params traz os dados para a conexão retirados do arquivo database.ini"""
        params = config()
        print("Conectando...")
        """A variavel conn irá conectar o postgre atraves do python utilizando os paramentros fornecidos"""
        conn = psycopg2.connect(**params)
        """O cursor ira iniciar a query para receber os comandos"""
        cur = conn.cursor() 
        print('PostgreSQL database version:')
        """o comando cur.excecute envia o comando a ser executado no PostgreSQL"""
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('Database connection closed')

if __name__ == '__main__':
    connect()