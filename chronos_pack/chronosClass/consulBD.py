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
            - ('Usuário encontrado', tuple): caso o usuario exista.
            - ('Usuário não encontrado', None): caso não exista.
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
        return e, None
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
        return e, None
    finally:
        cursor.close()
        conex.close()
        

def retorna_diario_byEmail(email_user:str):
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        query = """
        SELECT * FROM diario
        WHERE id_usuario =
        (SELECT id_usuario FROM usuario
        WHERE email = %s);
        """
        
        cursor.execute(query, (email_user,))
        diarios = cursor.fetchall()
        return diarios
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()
    

def retorna_materias_crono(id_cronograma:str):
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        query = """
        SELECT materias FROM cronograma
        WHERE id_cronograma = %s;
        """
        
        cursor.execute(query, (id_cronograma,))
        materias = cursor.fetchone()
        return "Materias encontradas", materias[0]
    except Exception as e:
        return e, None
    finally:
        cursor.close()
        conex.close()
    

def retorna_diarioinfo_userEmail(user_email:str):
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        query = """
        SELECT nome FROM diario
        WHERE id_usuario = 
        (SELECT id_usuario FROM usuario
        WHERE email = %s);
        """
        
        cursor.execute(query, (user_email,))
        diarios = cursor.fetchall()
        
        return diarios
    except Exception as e:
        return e, None
    finally:
        cursor.close()
        conex.close()
    
    
def retorna_chrono_diario(nome_diario:str):
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        query = """
        SELECT * FROM cronograma
        WHERE id_diario =
        (SELECT id_diario FROM diario
        WHERE nome = %s);
        """
        
        cursor.execute(query, (nome_diario,))
        chronos = cursor.fetchall()
        return chronos
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()