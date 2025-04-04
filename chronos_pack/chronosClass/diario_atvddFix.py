from datetime import date, datetime, time, timedelta
from manipBD import (registra_diario, registra_atividade_fixa,
atualiza_tempo_disponivel)
from verifBD import verify_diario, verify_usuario
from consulBD import retorna_diario

"""
Class Diario/Atividade_fixa
Esse módulo fornece a class Diario e
Atividade_fixa que possuem funcionalidades
para relações internas e com outras entidades
"""

class Diario:
    def __init__(
        self,
        nome:str, # Terá que ser único
        descricao:str,
        hora_acorda:datetime,
        hora_dorme:datetime
    ):
        self.nome = nome
        self.descricao = descricao
        self.data_registro = date.today()
        self.hora_acorda = hora_acorda
        self.hora_dorme = hora_dorme
        self._tempo_total = self.define_tempo_total()
        self._tempo_disponivel = 0 # Definido a partir de atividades fixas

    
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""


    def define_tempo_total(self) -> int:
        """
        Definição do _tempo_total
        
        Funcionalidade: faz a diferença
        da hora_dorme e hora_acorda (datetime)
        que resulta em um objeto timedelta
        
        Retorno:
            int: dif_horas em minutos
        """
        dif_horas = self.hora_dorme - self.hora_acorda
        return int(dif_horas.total_seconds()/60)
    
    
    @classmethod
    def criar(
        cls,
        nome:str,
        descricao:str,
        hora_acorda:str, # format %H:%M
        hora_dorme:str, # format %H:%M
        id_usuario:str
    ):
        """
        Criar Diario no BD
        
        Parâmetros:
            nome (str): nome do diario
            descricao (str): descricao do diario
            hora_acorda (str - HH:MM): hora que user acorda
            hora_dorme (str - HH:MM): hora que user dorme
            id_usuario (str): id ao qual o diario está vinculado
            
        Retornos:
            status de criação
        """
        diario_existe, _ = verify_diario(nome=nome)
        
        if not diario_existe:
            hora_acorda_date = datetime.strptime(hora_acorda, "%H:%M")
            hora_dorme_date = datetime.strptime(hora_dorme, "%H:%M")
            diario_criado = cls(nome, descricao, hora_acorda_date, hora_dorme_date)
            
            status = registra_diario(
                nome=nome,
                descricao=descricao,
                data_registro=diario_criado.data_registro,
                hora_acorda=hora_acorda,
                hora_dorme=hora_dorme,
                tempo_total=diario_criado._tempo_total,
                tempo_disponivel=diario_criado._tempo_total,
                id_usuario=id_usuario
            )
            
            return "Diário criado", status
        else:
            return "Diário já existe", ''
    

class Atividade_fixa:
    def __init__(
        self,
        nome:str,
        dia:str,
        hora_inicio:datetime,
        hora_final:datetime,
        nome_diario:str
    ):
        self.nome = nome
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.nome_diario = nome_diario
        self.tempo_consome = self.define_tempo_consome()
        
        
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""    
        
        
    def define_tempo_consome(self) -> int:
        """
        Definição do tempo_consome
        
        Funcionalidade: faz a diferença
        da hora_dorme e hora_acorda (datetime)
        que resulta em um objeto timedelta
        
        Retorno:
            int: dif_horas em minutos
        """
        dif_horas = self.hora_final - self.hora_inicio
        return int(dif_horas.total_seconds()/60)
    
    
    @classmethod
    def criar(
        cls,
        nome:str,
        dia:str,
        hora_inicio:str, # format %H:%M
        hora_final:str, # format %H:%M
        nome_diario:str
    ):
        """
        Criar Atividade Fixa no BD
        
        Parâmetros:
            nome (str): nome da atividade
            dia (str): dia da atividade
            hora_inicio (str): hora inicial HH:MM
            hora_final (str): hora final HH:MM 
            nome_diario (str): nome do diario para vínculo
            
        Retorno:
            status de inserção e de vínculo
        
        Except:
            None
        
        Obs:
            Não há como haver excessão, função
            chamada apênas sob certeza de existência
            do diário.
        """
        hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
        hora_final_dt = datetime.strptime(hora_final, '%H:%M')
        
        fixa_criada = cls(nome, dia, hora_inicio_dt, hora_final_dt, nome_diario)
        
        id_diario = retorna_diario(nome_diario)[1][0]
        print(fixa_criada.tempo_consome)
        
        status_insert = registra_atividade_fixa(
            nome=nome,
            dia=dia,
            hora_inicio=hora_inicio,
            hora_final=hora_final,
            tempo_consome=fixa_criada.tempo_consome,
            id_diario=id_diario
        )
        status_vinculo = atualiza_tempo_disponivel(
            id_diario=id_diario,
            tempo_consome=fixa_criada.tempo_consome
        )
        return status_insert, status_vinculo