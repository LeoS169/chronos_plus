import psycopg2 as pg2
from json import load

"""
Esse módulo possui funções para consultas
no banco de dados que possibilitam a validação
de dados informados pelo usuário
"""

with open("chronos_pack/chronosClass/connect.json", encoding="utf-8") as conexJson:
    db_conex = load(conexJson)
    

def verify_usuario(email:str):
    """
    Verifica usuario
    
    Parâmetros:
        email (str): email do user
        
    Retorno:
        True: user existe
        False: user não existe
    
    Excessão:
        emails = None 
    """
    global db_conex
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        query = "SELECT email FROM usuario;"
        cursor.execute(query)
        emails = cursor.fetchall()
        if emails:
            for email_bd in emails:
                if email_bd[0] == email:
                    return True
                else:
                    return False
        else:
            return False
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()
        

def verify_diario(nome:str):
    """
    Verifica diario
    
    Parâmetros:
        nome (str): nome do diario
        
    Retorno:
        True, str: diario existe
        False: diario não existe
    
    Excessão:
        id_diario = None 
    """
    global db_conex
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        query = """
            SELECT id_diario FROM diario
            WHERE nome = %s;
        """
        
        cursor.execute(query, (nome,))
        id_diario = cursor.fetchone()
        if id_diario:
            return True, id_diario[0]
        else:
            return False, ''
        
    except Exception as e:
        pass
    finally:
        cursor.close()
        conex.close()
        
        