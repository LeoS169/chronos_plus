from flet import Page
"""
Esse arquivo controla o fluxo entre as páginas
"""

def voltar_pagina_inicial(page: Page):
    from .inicial_page import pagina_inicial
    page.clean()
    pagina_inicial(page=page)
    

def go_entrar(page: Page):
    from .entrar_page import pagina_entrar
    page.clean()
    pagina_entrar(page=page)
    
    
def go_cadastro(page: Page):
    from .cadastro_page import pagina_cadastrar
    page.clean()
    pagina_cadastrar(page=page)