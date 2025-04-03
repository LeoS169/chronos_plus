from datetime import date
from verifBD import verify_usuario
from manipBD import registra_usuario, deleta_usuario

"""
Class Usuário
Esse módulo fornece a classe Usuário
Ela possui funções que possibilitam a alteração
e modificação da tabela homônimo no Banco de Dados 
"""

class Usuario:
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self._senha = senha
        self._data_criacao = date.today()
        
        
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"""
    
        
    @property 
    def senha(self):
        return self.senha


    @classmethod
    def criar(
        cls,
        nome:str,
        email:str,
        senha:str
    ):
        """
        Cria Usuário no BD
        
        Parâmetros:
            nome (str): nome do user
            email (str): email do user
            senha (str): senha do user
        
        Retorno:
            str: status de inserção
        
        Excessões:
            user_existe = True.
        """
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
        """
        Deleta Usuário do BD
        
        Parâmetros:
            email (str): email do user
            senha (str): senha do user
            
        Retorno:
            str: status de deleção
            
        Excessão:
            user_existe = False
        """
        user_existe = verify_usuario(email=email)
        if user_existe:
            status = deleta_usuario(
                email=email,
                senha=senha
            )
            return 'Usuário deletado', status
        else:
            return "Usuário não existe!"
    
    
    
    

    
        
