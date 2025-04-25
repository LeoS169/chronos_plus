import sys, os
from json import load
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .assets.tools.conv import cria_container_elementos, cria_botao, cria_atividade
from chronos_pack.chronosClass.consulBD import retorna_diario_byEmail
from flet import Page, MainAxisAlignment, Row, Column, Text, ScrollMode, Container, app
from .fluxo import go_pagina_principal

# Dados user
with open("pages/userinfo.json", "r") as f_user:
    arq = load(f_user)
    email = arq['user']
    qntDiario = arq['qntDiario']
    diarioAtivo = arq['diarioAtivo']
    
diarios_user = retorna_diario_byEmail(email)
lista_diarios = []

def voltar(page: Page):
    """
    Função do botão de voltar
    
    Ao chamar a função, a lista de 
    diarios é resetada e vai para
    a página principal
    """
    global lista_diarios
    lista_diarios = []
    go_pagina_principal(page=page)

def pagina_diario(page: Page):
    page.title = "Chronos+"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#222333"
    page.window.full_screen = True
    page.fonts = {
        "Jersey10": "pages/assets/fonts/Jersey10-Regular.ttf",
        "Jersey15": "pages/assets/fonts/Jersey15-Regular.ttf",
        "Jersey25": "pages/assets/fonts/Jersey25-Regular.ttf"
    }
    
    # Elementos da Row superior
    diario_name = Text(
        "_Diários",
        font_family="Jersey15",
        size=75
    )
    
    qnt_diarios = Text(
        f"Quantidade de diários: {qntDiario}",
        font_family="Jersey15",
        size=60
    )
    
    novo_diario_btn = cria_botao(
        "_Novo", None
    )
    novo_diario_btn.style.bgcolor = "#006913"
    novo_diario_btn.content.size = 40
    novo_diario_btn.width = 120
    novo_diario_btn.height = 45
    
    # Elementos do Container sobreposto ao principal
    ativar_btn = cria_botao("_Ativar", None)
    ativar_btn.width = 130
    ativar_btn.height = 50
    ativar_btn.content.size = 40
    ativar_btn.style.bgcolor = "#006913" 
    
    if diarios_user:
        for i in range(len(diarios_user)):
            nome = diarios_user[i][1]
            atividade = "ativo" if nome == diarioAtivo else "inativo"
            tempo_dec = int(diarios_user[i][6])/60
            tempo_int = int(tempo_dec)
            minutos = (tempo_dec - tempo_int) * 60
            diario = cria_atividade(
                Row(
                    [
                        Text(f"{i}", font_family="Jersey15", size=50),
                        Text(f"{nome}", font_family="Jersey15", size=50),
                        ativar_btn,
                        Text(atividade, font_family="Jersey15", size=50),
                        Text(f"Tempo total: {tempo_int}h{minutos:.0f}min", 
                            font_family="Jersey15", size=50)
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=100
                )
            )    
            lista_diarios.append(diario)
    
    
    voltar_botao = cria_botao(
        "Voltar", 
        lambda e: voltar(page=page)
    )
    voltar_botao.width = 200
    voltar_botao.height = 60
    voltar_botao.content.size = 50
    voltar_botao.style.overlay_color = "#971717"
    
    # Container sobreposto ao principal
    container_sobr = cria_container_elementos(
        Column(
            [
                Column(
                    controls=lista_diarios, # Lista de diarios
                    height=440,
                    scroll=ScrollMode.HIDDEN,
                    spacing=30
                ),
                Row(
                    [voltar_botao],
                    alignment=MainAxisAlignment.END
                )
            ]
        )
    )
    container_sobr.bgcolor = "#222333"
    container_sobr.height = 550
    container_sobr.width = 1150
    container_sobr.padding = 20
    
    # Container principal
    main_container = cria_container_elementos(
        Column([
            Row([diario_name, qnt_diarios, novo_diario_btn],
                alignment=MainAxisAlignment.CENTER,
                spacing=180),
            Row(
                [container_sobr],
                MainAxisAlignment.CENTER
            )
        ])
    )
    main_container.margin = 20
    main_container.padding = 5
    main_container.width = 1200
    main_container.height = 680
    
    page.add(
        Row(
            [main_container],
            alignment=MainAxisAlignment.CENTER
        )
    )
