from datetime import datetime
from manipBD import (registra_cronograma,
registra_task, atualiza_tempo_necessario,
atualiza_tempo_disponivel)
from consulBD import retorna_diario

class Cronograma:
    def __init__(
      self,
      nome:str,
      descricao:str,
      materias:list,
      data_inicio:datetime,
      data_fim:datetime
    ):
        self.nome = nome
        self.descricao = descricao
        self.materias = materias
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tempo_necessario = 0 # Soma de tempos das tasks
        
        
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""
        
    
    @classmethod
    def criar(
        cls,
        nome:str,
        descricao:str,
        materias:list, # Lista objetos str()
        data_inicio:str, # format %d/%m/%Y
        data_fim:str, # format %d/%m/%Y
        id_usuario:str,
        nome_diario:str
    ):
        """
        Criar Cronograma no BD
        
        Parâmetros:
            nome (str): nome do cronograma
            descricao (str): descricao do cronograma
            materias (str): escopo de matérias
            data_inicio (str): inicio do cronograma
            data_fim (str): fim do cronograma
            id_usuario (str): id do user logado
            nome_diario (str): nome do diário ativo
            
        Retornos:
            str: status de inserção
        
        Excessão:
            except Exception

        Obs:
            materias define o escopo de
            escolhas da Task vinculada ao cronograma
        """
        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")
        crono_criado = cls(nome, descricao, materias, data_inicio, data_fim)
        
        id_diario = retorna_diario(nome_diario)[1][0]
        
        status = registra_cronograma(
            nome=nome,
            descricao=descricao,
            materias=materias,
            data_inicio=data_inicio,
            data_fim=data_fim,
            tempo_necessario=crono_criado.tempo_necessario,
            id_usuario=id_usuario,
            id_diario=id_diario
        )
        return status
    

class Task:
    def __init__(
        self,
        nome:str,
        descricao:str,
        materia:str,
        dia:str,
        hora_inicio:datetime,
        hora_final:datetime,
        id_cronograma:str
    ):
        self.nome = nome
        self.descricao = descricao
        self.materia = materia
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.tempo_previsto = self.define_tempo_previsto()
        self.status = "pendente" # Valor default
        self.prioridade = "baixa" # Valor default
        self.id_cronograma = id_cronograma
    
    
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""
    
    
    def define_tempo_previsto(self) -> int:
        dif_horas = self.hora_final - self.hora_inicio
        return int(dif_horas.total_seconds()/60)
    
    @classmethod
    def criar(
        cls,
        nome:str,
        descricao:str,
        materia:str,
        dia:str,
        hora_inicio:str, # format %H:%M
        hora_final:str, # format %H:%M
        id_cronograma:str,
        nome_diario:str
    ):
        """
        Criar Task no BD
        
        Parâmetros:
            nome (str): nome do cronograma
            descricao (str): descricao do cronograma
            materia (str): materia da task
            hora_inicio (str): inicio da task
            hora_final (str): fim da task
            id_cronograma (str): id do cronograma ativo
            nome_diario (str): nome do diário ativo
            
        Retornos:
            tuple:
                (str, str, str): status de inserção,
                atualização do diario e do cronograma
        
        Excessão:
            None
        """
        # Conversão das horas
        hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
        hora_final_dt = datetime.strptime(hora_final, '%H:%M')
        # Pega id_diario
        id_diario = retorna_diario(nome_diario)[1][0]
        # Cria objeto
        task_criada = cls(
            nome,
            descricao,
            materia,
            dia,
            hora_inicio_dt,
            hora_final_dt,
            id_cronograma
        )
        # Faz o insert
        status_insert = registra_task(
            nome=nome,
            descricao=descricao,
            materia=materia,
            dia=dia,
            status=task_criada.status,
            prioridade=task_criada.prioridade,
            hora_inicio=hora_inicio,
            hora_final=hora_final,
            tempo_previsto=task_criada.tempo_previsto,
            id_cronograma=id_cronograma
        )
        # Adiciona tempo necessário
        status_att = atualiza_tempo_necessario(
            id_cronograma,
            task_criada.tempo_previsto
        )
        # Subtrai do tempo disponível
        status_vinc = atualiza_tempo_disponivel(
            id_diario=id_diario,
            tempo_consome=task_criada.tempo_previsto
        )
        # Status das funcções
        return status_insert, status_att, status_vinc

