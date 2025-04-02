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


    def define_hora_total(self):
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
    


        