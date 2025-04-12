from flet import Row, Page, MainAxisAlignment, Text, app
from .assets.tools.conv import cria_container

def pagina_entrar(page:Page):
    page.title = "Chronos+"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.fonts = {
        "Jersey10": "pages/assets/fonts/Jersey10-Regular.ttf",
        "Jersey15": "pages/assets/fonts/Jersey15-Regular.ttf",
        "Jersey25": "pages/assets/fonts/Jersey25-Regular.ttf"
    }
    
    
    entrar_name = Text(
        value="_Entrar",
        font_family="Jersey15",
        size=100
    )
    
    container_valores = cria_container(
        None
    )
    
    page.add(
       Row(
           controls=[entrar_name],
           alignment=MainAxisAlignment.CENTER
       ),
       Row(
           controls=[container_valores],
           alignment=MainAxisAlignment.CENTER
       )
    )
    
