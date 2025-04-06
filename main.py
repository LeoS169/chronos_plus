import flet as ft
from pages.inicial_page import pagina_inicial

def chronos_plus(page: ft.Page):
    pagina_inicial(page=page)
    

ft.app(
    target=chronos_plus
)