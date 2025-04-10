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
        size=110
    )
    
    
    column_esquerda =  ft.Column(
        controls=[chronos_name],
        alignment=ft.MainAxisAlignment.CENTER
    );
    
    column_direita = ft.Column(
        controls=[],
        alignment=ft.MainAxisAlignment.CENTER
    );
    
    page.add(
        ft.Row(
            [
                column_esquerda,
                column_direita
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    
