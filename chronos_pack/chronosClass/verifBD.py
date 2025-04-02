import psycopg2 as pg2
import json

with open("chronos_pack/chronosClass/connect.json", encoding="utf-8") as conexJson:
    db_conex = json.load(conexJson)
    

def verify_usuario(email:str):
    global db_conex
    # Recebe email do user
    # Retorna True se email existir
    # Retorna False se não existir
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        query = "SELECT email FROM usuarios;"
        cursor.execute(query)
        emails = cursor.fetchall()
        if emails:
            for email_bd in emails:
                if email_bd == email:
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
        
