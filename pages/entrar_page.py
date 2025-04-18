import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .assets.tools.conv import cria_container_elementos, cria_container_entrada, cria_botao, open_snack_bar
from .assets.tools.defUserinfo import define_userinfo
from chronos_pack.chronosClass.consulBD import retorna_usuario, retorna_diarioinfo_userEmail
from flet import Row, Page, MainAxisAlignment, Text, Column, ScrollMode, TextField, app
from .fluxo import voltar_pagina_inicial, go_principal_page 

"""
Script com pagina de login.
Aparece ao clicar botão entrar da
página inicial.
"""

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
    
    
    def func_login_botao(
        email_entrada:TextField,
        senha_entrada:TextField
    ):
        email = email_entrada.value
        senha = senha_entrada.value
        
        if not email or not senha:
            open_snack_bar(
                page=page,
                texto="Campos obrigatórios não preenchidos",
                cor='#971717'
            )
        else:
            _, user = retorna_usuario(email, senha)
            if not user:
                open_snack_bar(
                    page=page,
                    texto=f"Email ou senha invalido!",
                    cor="#971717"
                )
            else:
                diarios = retorna_diarioinfo_userEmail(email)
                diarioAtivo = diarios[0][0] if diarios else 'nenhum!'
                qntDiario = len(diarios) if diarios else 0
                define_userinfo(
                    user=email,
                    senha=senha,
                    diarioAtivo=diarioAtivo,
                    qntDiario=qntDiario
                )
                go_principal_page(page=page)
            # Abre página principal
        
        page.update()
            
    
    # Texto da página de entrar
    entrar_name = Text(
        value="_Entrar",
        font_family="Jersey15",
        size=100
    )
    
    # Containers de entrada
    entrada_email_container = cria_container_entrada(
        "_E-mail", "Jersey10"
    )
    entrada_senha_container = cria_container_entrada(
        "_Password", "Jersey10"
    )
    
    # TextFields do cria_container_entrada
    email_txtField = entrada_email_container.content.controls[1]
    senha_txtField = entrada_senha_container.content.controls[1]

    
    # Botões de Login e Voltar
    login_botao = cria_botao(
        "Login",
        funcao=lambda e: func_login_botao(
            email_entrada=email_txtField,
            senha_entrada=senha_txtField
        )
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
    
    # Container principal, que porta entradas
    container_valores = cria_container_elementos(
        Column(
            controls=[
                entrada_email_container,
                entrada_senha_container,
                Row(
                    [login_botao, voltar_botao],
                    alignment=MainAxisAlignment.CENTER
                )
                ],
            spacing=40,
            auto_scroll=ScrollMode.AUTO
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
    
