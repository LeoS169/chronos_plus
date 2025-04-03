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
        return 'Insert confirmed'
    except Exception as e:
        return e
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
        

def deleta_usuario(
    email:str,
    senha:str
):
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        _, usuario = retorna_usuario(
            email=email,
            senha=senha
        )
        
        if usuario:
            query = """
                DELETE FROM usuario WHERE email = %s AND senha = %s;
            """
            cursor.execute(query, (email, senha,))
            conex.commit()
            return 'Delete confirmed'
        else:
            return 'Erro: usuario não encontrado'
        
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()

    
    
    
    