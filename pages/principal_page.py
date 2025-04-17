import sys, os
from json import load
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from assets.tools.conv import cria_container_elementos
from flet import app, Page, MainAxisAlignment, CrossAxisAlignment, Row, Column, Text


def pagina_principal(page:Page):
    page.title = "Chronos+"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.window.full_screen = True
    page.fonts = {
        "Jersey10": "pages/assets/fonts/Jersey10-Regular.ttf",
        "Jersey15": "pages/assets/fonts/Jersey15-Regular.ttf",
        "Jersey25": "pages/assets/fonts/Jersey25-Regular.ttf"
    }
    
    # Textos da coluna superior
    texto_ola = Text(
        "Olá, NOME!",
        font_family="Jersey15",
        size=100
    )
    
    diario_ativo_txt = Text(
        "Diário ativo: nenhum",
        font_family="Jersey15",
        size=60
    )
    horas_estu_txt = Text(
        "Horas estudadas: 2h",
        font_family="Jersey15",
        size=60
    )
    horas_restantes_txt = Text(
        "Horas restantes: 8h",
        font_family="Jersey15",
        size=60
    )
    
    # Colunas da Row superior
    coluna_superiorA = Column(
        [texto_ola],
        horizontal_alignment=CrossAxisAlignment.CENTER
    )
    
    coluna_superiorB = Column(
        [
            diario_ativo_txt,
            horas_estu_txt,
            horas_restantes_txt
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=0
    )
    
    # COntainer principal
    main_container = cria_container_elementos(
        Column(
            [
                Row( # Row superior
                    [coluna_superiorA, coluna_superiorB],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=250
                ),
                Row()
            ]  
        )
    )
    main_container.margin = 30
    main_container.width = 1200
    main_container.height = 680
    
    page.add(
        Row(
            [main_container],
            alignment=MainAxisAlignment.CENTER
        )
    )
    
    
app(pagina_principal)