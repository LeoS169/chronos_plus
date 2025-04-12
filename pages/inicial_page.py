import flet as ft
from .assets.tools.conv import cria_botao, cria_container
from .fluxo import go_entrar

"""
Script com página inicial
do Chronos+ com botões de login
e sign in
"""

def pagina_inicial(page: ft.Page):
    page.title = "Chronos+"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.fonts = {
        "Jersey10": "pages/assets/fonts/Jersey10-Regular.ttf",
        "Jersey15": "pages/assets/fonts/Jersey15-Regular.ttf",
        "Jersey25": "pages/assets/fonts/Jersey25-Regular.ttf"
    }


    # Nome titulo
    chronos_name = ft.Text(
        value='_CHRONOS+',
        font_family="Jersey25",
        size=140
    )
    
    # Botões
    entrar_botao = cria_botao(
        "_Entrar",
        funcao=lambda e: go_entrar(page=page)
        )
    cadastrar_botao = cria_botao("_Cadastrar", None)
    
    # Container com botões de entrar e cadastrar
    container_bot = cria_container(
        ft.Column(
            width=560,
            controls=[entrar_botao, cadastrar_botao],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40
        )
    )
    
    # Coluna da esquerda
    column_esquerda =  ft.Column(
        controls=[chronos_name],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    # Coluna da direita
    column_direita = ft.Column(
        controls=[container_bot],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    # Container da esquerda
    container_esquerda = ft.Container(
        content=column_esquerda,
        expand=1,
        margin=ft.margin.only(top=50)
    )
    
    # Container da direita
    container_direita = ft.Container(
        content=column_direita,
        expand=1
    )
    
    # Adição de elementos
    page.add(
        ft.Row(
            [
                container_esquerda,
                container_direita
            ], expand=True
        )
    )
    

