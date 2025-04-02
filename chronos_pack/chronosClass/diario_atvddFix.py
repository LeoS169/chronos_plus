from datetime import date, datetime, time, timedelta


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
        self._tempo_total = self.define_hora_total()
        self._tempo_disponivel = 0 # Definido a partir de atividades fixas

    
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""


    def define_hora_total(self) -> int:
        # Efetua a diferença
        # Retorna minutos
        dif_horas = self.hora_dorme - self.hora_acorda
        return int(dif_horas.total_seconds()/60)
    
    
    @classmethod
    def criar(
        cls,
        nome:str,
        descricao:str,
        hora_acorda:str, # format %H:%M
        hora_dorme:str, # format %H:%M
    ):
        # Converte hora_acorda e hora_dorme
        # Registra Diario no BD
        hora_acorda = datetime.strptime(hora_acorda, "%H:%M")
        hora_dorme = datetime.strptime(hora_dorme, "%H:%M")
        pass
    

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
        self.hora_inicio = hora_inicio,
        self.hora_final = hora_final
        self.nome_diario = nome_diario
        self.tempo_consome = self.define_tempo_consome()
        
        
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""    
        
        
    def define_tempo_consome(self) -> int:
        # Efetua diferença
        # Retorna minutos
        dif_horas = self.hora_final - self.hora_final
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
        # Converte hora_inicio e hora_final
        # Registra no Atividade no BD
            # O registro precisa verificar se o BD existe
            # Ao registrar, ele define tempo disponivel
            # Se sim, função retorna ID, o que possibilita registro
        pass