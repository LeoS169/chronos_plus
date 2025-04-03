import psycopg2 as pg2
from json import load

# Esse arquivo possui funções para consultas
# no banco de dados que possibilitam a validação
# de dados informados pelo usuário

with open("chronos_pack/chronosClass/connect.json", encoding="utf-8") as conexJson:
    db_conex = load(conexJson)
    

def verify_usuario(email:str):
    global db_conex
    # Recebe email do user
    # Retorna True se email existir
    # Retorna False se não existir
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
    global db_conex
    # Recebe o nome do diario
    # Retorna True, id_diario se ele existir
    # Retorna False se não
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
        
        
def retorna_usuario(email:str, senha:str):
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