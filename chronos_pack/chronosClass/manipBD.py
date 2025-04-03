import psycopg2 as pg2
from json import load

with open("chronos_pack/chronosClass/connect.json", encoding="utf-8") as conexJson:
    db_conex = load(conexJson)

def registra_usuario(
    nome:str,
    email:str,
    senha:str,
    data_criacao:str # format 'yyyy-mm-dd'
):
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        query = """
            INSERT INTO usuario (nome, email, senha, data_criacao)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (nome, email, senha, data_criacao,))
        conex.commit()
        return 'ok'
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()
    
    
    