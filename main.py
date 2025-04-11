import flet as ft
from pages.inicial_page import pagina_inicial

def chronos_plus(page: ft.Page):
    """
    Inicializador Aplicativo
    
    Cria página com o Flet (ft.Page)
    para ser inicializado. Usa a pagina
    inicial como página de abertura
    """
    pagina_inicial(page=page)
    

ft.app(
    target=chronos_plus
)