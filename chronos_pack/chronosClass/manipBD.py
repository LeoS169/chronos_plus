import psycopg2 as pg2
from json import load
from consulBD import retorna_usuario

"""
Esse módulo possui as funções de manipulações
diretas ao Banco de dados. Insert, Delete e 
Alter.
"""

with open("chronos_pack/chronosClass/connect.json", encoding="utf-8") as conexJson:
    db_conex = load(conexJson)

def registra_usuario(
    nome:str,
    email:str,
    senha:str,
    data_criacao:str # format 'yyyy-mm-dd'
):
    """
    Registra usuario
    
    Parâmetros:
        nome (str): nome do user
        email (str): email do user
        senha (str): senha do user
        data_criacao (str): data_criacao do user
        
    Retornos:
        str: status de inserção
        
    Excessão:
        except Exeption
    """
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
        

def deleta_usuario(
    email:str,
    senha:str
):
    """
    Deleta usuario
    
    Parâmetro: 
        email (str): email do user
        senha (str): senha do user
    
    Retorno:
        str: status de deleção
        
    Excessão:
        except Exception
    """
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


def registra_diario(
    nome:str,
    descricao:str,
    data_registro:str,
    hora_acorda:str,
    hora_dorme:str,
    tempo_total:str,
    tempo_disponivel:str,
    id_usuario:str
):
    """
    Registra diario
    
    Parâmetro: 
        nome (str): nome do diario
        descricao (str): descricao do diario
        data_registro (str): data do registro
        hora_acorda (str): hora que o user acorda
        hora_dorme (str): hora que o user dorme
        tempo_total (str): hora_dorme - hora_acorda
        id_usuario (str): id para vincular ao diario
    
    Retorno:
        str: status de registro
        
    Excessão:
        except Exception
    """
    try:
        conex = pg2.connect(**db_conex)
        cursor  = conex.cursor()
        
        query = """
            INSERT INTO diario (nome, descricao, data_registro, hora_acorda, 
            hora_dorme, tempo_total, tempo_disponivel, id_usuario)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        cursor.execute(
            query,
            (
                nome,
                descricao,
                data_registro,
                hora_acorda,
                hora_dorme,
                tempo_total,
                tempo_disponivel,
                id_usuario
            )
        )
        conex.commit()
        return 'Insert confirmed'
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()
    

def registra_atividade_fixa(
    nome:str,
    dia:str,
    hora_inicio:str,
    hora_final:str,
    tempo_consome:str,
    id_diario:str
):
    """
    Registra Atividade fixa
    
    Parâmetros:
        nome (str): nome da atividade
        dia (str): dia 
        hora_inicio (str): hora inicial HH:MM 
        hora_final (str): hora final HH:MM
        tempo_consome (str): tempo consumido
        id_diario (str): id do diario
        
    Retorno:
        stt: status de inserção
    
    Excessão:
        except Exception
        
    Obs:
        dia (str) no escopo ['segunda',
        'terça', 'quarta, 'quinta',
        'sexta', 'sábado', 'domingo']
    """
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        query = """
            INSERT INTO atividade_fixas (nome, dia, hora_inicio, 
            hora_final, tempo_consome, id_diario)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        
        cursor.execute(
            query,
            (
                nome,
                dia,
                hora_inicio,
                hora_final,
                tempo_consome,
                id_diario
            )
        )
        conex.commit()
        return "Insert confirmed"
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()
    
    
def atualiza_tempo_disponivel(
    id_diario:str,
    tempo_consome:str
):
    """
    Vincula Atividade Diario
    
    Parâmetros:
        id_diario (str): id do diário
        tempo_consome (str): tempo que atividade consome
        
    Retorno:
        str: status de inserção
    
    Excessão:
        except Exception
        se tempo_disponivel < tempo_consome
    """
    try:
        conex = pg2.connect(**db_conex)
        cursor = conex.cursor()
        
        # Requisição de dados do diario
        query = """
        SELECT tempo_disponivel FROM diario
        WHERE id_diario = %s;
        """
        cursor.execute(query, (id_diario,))
        dados = cursor.fetchone()
        
        tempo_disponivel = int(dados[0])
        tempo_consome = int(tempo_consome)
        
        # Atualização dos dados
        if tempo_disponivel >= tempo_consome:
            tempo_disponivel -= tempo_consome
            
            query = """
            UPDATE diario
            SET tempo_disponivel = %s
            WHERE id_diario = %s;
            """
            cursor.execute(query, (tempo_disponivel, id_diario,))
            conex.commit()
            return "Tempo diário atualizado"
        else:
            return "Tempo inválido!"
    except Exception as e:
        return e
    finally:
        cursor.close()
        conex.close()
    

    