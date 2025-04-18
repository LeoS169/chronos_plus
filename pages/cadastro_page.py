import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .assets.tools.defUserinfo import define_userinfo
from chronos_pack.chronosClass.usuario import Usuario
from chronos_pack.chronosClass.consulBD import retorna_usuario
from flet import Row, Page, MainAxisAlignment, Text, Column, ScrollMode, TextField, app
from .assets.tools.conv import cria_container_elementos, cria_container_entrada, cria_botao, open_snack_bar
from .fluxo import go_pagina_inicial, go_principal_page 

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
        nome_entrada:TextField,
        email_entrada:TextField,
        senha_entrada:TextField
        
    ):
        nome = nome_entrada.value
        email = email_entrada.value
        senha = senha_entrada.value
        
        if not nome or not email or not senha:
            open_snack_bar(
                page=page,
                texto="Campos obrigatórios não preenchidos",
                cor='#971717'
            )
        else:
            status, status_ins = Usuario.criar(
                nome=nome,
                email=email,
                senha=senha
            )
            if status_ins:
                open_snack_bar(
                    page=page,
                    texto=status,
                    cor="#006913"
                )
                define_userinfo(
                    user=email,
                    senha=senha,
                    diarioAtivo='nenhum!',
                    qntDiario=0 
                )
                go_principal_page(page=page)
            else:
                open_snack_bar(
                    page=page,
                    texto=status,
                    cor="#971717"
                )
        page.update()
            
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
    
    # TextFields das entradas
    nome_txtField = entrada_nome_container.content.controls[1]
    email_txtField = entrada_email_container.content.controls[1]
    senha_txtField = entrada_senha_container.content.controls[1]
    
    # Botões de Login e Voltar
    sign_botao = cria_botao(
        texto="Sign In",
        funcao=lambda e: func_sign_botao(
            nome_entrada=nome_txtField,
            email_entrada=email_txtField,
            senha_entrada=senha_txtField
        )
    )
    sign_botao.width = 220
    sign_botao.height = 60
    sign_botao.content.size = 50

    
    voltar_botao = cria_botao(
        "Voltar", lambda e: go_pagina_inicial(page)
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
    