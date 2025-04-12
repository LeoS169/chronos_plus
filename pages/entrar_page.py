from flet import(Row, Page, MainAxisAlignment,
    Text, Column, ScrollMode, app)

from .assets.tools.conv import (cria_container_elementos,
    cria_container_entrada, cria_botao)

from .fluxo import voltar_pagina_inicial 

def pagina_entrar(page:Page):
    page.title = "Chronos+"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.window.full_screen = True
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
    
    entrada_email = cria_container_entrada(
        "_E-mail", "Jersey10"
    )
    
    entrada_senha = cria_container_entrada(
        "_Password", "Jersey10"
    )
    
    login_botao = cria_botao(
        "Login", None
    )
    login_botao.width = 220
    login_botao.height = 60
    login_botao.content.size = 50

    
    voltar_botao = cria_botao(
        "Voltar", lambda e: voltar_pagina_inicial(page)
    )
    voltar_botao.width = 200
    voltar_botao.height = 60
    voltar_botao.content.size = 50
    voltar_botao.style.overlay_color = "#971717"
    
    container_valores = cria_container_elementos(
        Column(
            controls=[
                entrada_email,
                entrada_senha,
                Row(
                    [login_botao, voltar_botao],
                    alignment=MainAxisAlignment.CENTER
                )
                ],
            spacing=40,
            auto_scroll=ScrollMode.AUTO
        )
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
    
