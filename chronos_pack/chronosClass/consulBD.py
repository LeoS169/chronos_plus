import psycopg2 as pg2
from json import load

"""
Esse módulo possui as funções de consulta e 
retorno de elementos no BD.
"""

with open("chronos_pack/chronosClass/connect.json", encoding="utf-8") as conexJson:
    db_conex = load(conexJson)


def retorna_usuario(email:str, senha:str):
    """
    Retorna usuario
    
    Parâmetros:
        email (str): email do user
        senha (str): senha do user
        
    Retorno:
        str, tuple -> user existe
        str, None -> user não existe
    
    Excessão:
        Exception 
    """
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        query = """
            SELECT * FROM usuario WHERE email = %s AND senha = %s;
        """
        cursor.execute(query, (email, senha))
        user = cursor.fetchone()
        return 'Usuario encontrado', user
    except Exception as e:
        return e, ''
    finally:
        cursor.close()
        conex.close()