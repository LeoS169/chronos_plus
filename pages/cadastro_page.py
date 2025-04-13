from flet import(Row, Page, MainAxisAlignment,
    Text, Column, ScrollMode, app)

from .assets.tools.conv import (cria_container_elementos,
    cria_container_entrada, cria_botao)

from .fluxo import voltar_pagina_inicial 

"""
Script com pagina de cadastro.
Aparece ao clicar botão cadastrar da
página inicial.
"""

def pagina_cadastrar(page:Page):
    page.title = "Chronos+"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.window.full_screen = True
    page.fonts = {
        "Jersey10": "pages/assets/fonts/Jersey10-Regular.ttf",
        "Jersey15": "pages/assets/fonts/Jersey15-Regular.ttf",
        "Jersey25": "pages/assets/fonts/Jersey25-Regular.ttf"
    }
    
    
    def func_sign_botao(
        
    ):
        pass
    
    # Texto da página de entrar
    entrar_name = Text(
        value="_Cadastrar",
        font_family="Jersey15",
        size=100,
        color="#FFFFFF"
    )
    
    # Containers de entrada
    entrada_nome_container = cria_container_entrada(
        "_Nome", "Jersey10"
    )
    
    entrada_email_container = cria_container_entrada(
        "_E-mail", "Jersey10"
    )
    
    entrada_senha_container = cria_container_entrada(
        "_Password", "Jersey10"
    )
    
    # Botões de Login e Voltar
    sign_botao = cria_botao(
        "Sign In", None
    )
    sign_botao.width = 220
    sign_botao.height = 60
    sign_botao.content.size = 50

    
    voltar_botao = cria_botao(
        "Voltar", lambda e: voltar_pagina_inicial(page)
    )
    voltar_botao.width = 200
    voltar_botao.height = 60
    voltar_botao.content.size = 50
    voltar_botao.style.overlay_color = "#971717"
    
    # Container principal, que porta entradas
    container_valores = cria_container_elementos(
        Column(
            controls=[
                entrada_nome_container,
                entrada_email_container,
                entrada_senha_container,
                Row(
                    [sign_botao, voltar_botao],
                    alignment=MainAxisAlignment.CENTER
                )
                ],
            spacing=40,
            scroll=ScrollMode.HIDDEN
        )
    )
    
    # Adição da página
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
    