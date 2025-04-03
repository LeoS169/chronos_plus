from datetime import date
from verifBD import verify_usuario
from manipBD import registra_usuario, deleta_usuario

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
    def criar(
        cls,
        nome:str,
        email:str,
        senha:str
    ):
        # Verifica se usuário existe
        # Converte data_criacao para o BD
        # Registra User no BD
        user_existe = verify_usuario(email=email)
        if not user_existe:
            user = cls(nome, email, senha)
            data_criacao = user._data_criacao.strftime('%Y-%m-%d')
            
            status = registra_usuario(
                nome=nome,
                email=email,
                senha=senha,
                data_criacao=data_criacao
            )
            return "Usuário criado", status
        else:
            return "Usuário já existe!", ''
    
    
    def deletar(
        self,
        email:str,
        senha:str
    ):
        # Verifica se usuário existe
        # Deleta usuário
        user_existe = verify_usuario(email=email)
        if user_existe:
            status = deleta_usuario(
                email=email,
                senha=senha
            )
            return 'Usuário deletado', status
        else:
            return "Usuário não existe!"
    
    @property 
    def senha(self):
        return self.senha
    
    
    

    
        
