import flet as ft

def pagina_inicial(page: ft.Page):
    page.title = "Chronos+"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.fonts = {
        "Jersey10": "pages/fonts/Jersey10-Regular.ttf",
        "Jersey15": "pages/fonts/Jersey15-Regular.ttf",
        "Jersey25": "pages/fonts/Jersey25-Regular.ttf"
    }


    # Nome titulo
    chronos_name = ft.Text(
        value='_CHRONOS+',
        font_family="Jersey25",
        size=140
    )
    
    # Container com botões de entrar e cadastrar
    container_bot = ft.Container(
        bgcolor="#25274A",
        width=560,
        height=540,
        border_radius=30
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
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=1
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
    
    
