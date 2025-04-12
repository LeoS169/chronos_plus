from flet import Page
from .entrar_page import pagina_entrar

"""
Esse arquivo controla o fluxo entre as páginas
"""

def go_entrar(page: Page):
    page.clean()
    pagina_entrar(page=page)