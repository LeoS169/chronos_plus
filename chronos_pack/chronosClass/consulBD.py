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
        tuple:
            - ('Diário encontrado', tuple): caso o usuario exista.
            - ('Diário não encontrado', None): caso não exista.
            - (Exception, str): em caso de erro na execução.
    
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
        

def retorna_diario(nome:str):
    """
    Retorna diário
    
    Parâmetro:
        nome (str): nome do diario
        
    Retorno:
        tuple:
            - ('Diário encontrado', tuple): caso o diário exista.
            - ('Diário não encontrado', None): caso não exista.
            - (Exception, str): em caso de erro na execução.
    
    """
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        query = """
            SELECT * FROM diario WHERE nome = %s;
        """
        cursor.execute(query, (nome,))
        diario = cursor.fetchone()
        return 'Diario encontrado', diario
    except Exception as e:
        return e, ''
    finally:
        cursor.close()
        conex.close()