from datetime import datetime
from manipBD import registra_cronograma
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
        nome_cronograma:str
    ):
        self.nome = nome
        self.descricao = descricao
        self.materia = materia
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.tempo_previsto = 0
        self.status = "pendente" # Valor default
        self.prioridade = "baixa" # Valor default
        self.nome_cronograma = nome_cronograma
    
    
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""
    
    
    @classmethod
    def criar(
        cls,
        nome:str,
        descricao:str,
        materia:str,
        dia:str,
        hora_inicio:str, # format %H:%M
        hora_final:str, # format %H:%M
        nome_cronograma:str
    ):
        # Verifica se materia está dentro do escopo do cronograma referido
        # Registra no BD
        # Verifica se tempo previsto cabe em tempo_necessario
        # Adiciona tempo_previsto ao tempo_necessario do cronograma
        pass