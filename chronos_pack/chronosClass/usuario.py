from datetime import date

class Usuario:
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self._senha = senha
        self._data_criacao = date.today()
        
        
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""
        

    @classmethod
    def cria_usuario(
        cls,
        nome:str,
        email:str,
        senha:str
    ):
        # Verifica se usuário existe
        # Registra User em BD
        pass
    
    
    @property 
    def senha(self):
        return self.senha
    
    

    
        
