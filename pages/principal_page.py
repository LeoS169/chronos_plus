import sys, os
from json import load
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .assets.tools.conv import cria_container_elementos, cria_botao
from chronos_pack.chronosClass.consulBD import retorna_usuario
from flet import app, Page, MainAxisAlignment, CrossAxisAlignment, Row, Column, Text

# Dados do user:
with open("pages/userinfo.json", "r") as f_user:
    arq = load(f_user)
    email = arq['user']
    senha = arq['senha']
    _, user = retorna_usuario(email, senha)
    nome = user[1]
    qnt_diario = arq['qntDiario']
    diarioAtivo = arq['diarioAtivo']
    
    
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
        f"Olá, {nome}",
        font_family="Jersey15",
        size=100
    )
    
    diario_ativo_txt = Text(
        f"Diário ativo: {diarioAtivo}",
        font_family="Jersey15",
        size=50
    )
    horas_estu_txt = Text(
        "Horas estudadas: 2h",
        font_family="Jersey15",
        size=50
    )
    horas_restantes_txt = Text(
        "Horas restantes: 8h",
        font_family="Jersey15",
        size=50
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
        ]
    )
    
    # Botoes
    
    diario_btn = cria_botao("_Diário", None)
    chronos_btn = cria_botao("_Chronos", None)
    estati_btn = cria_botao("_Estatísticas", None)
    _ = cria_botao("_NãoSei", None)
    
    coluna_inferior_esq = Column(
        [diario_btn, chronos_btn],
        alignment=MainAxisAlignment.CENTER,
        spacing=75
    )
    
    coluna_inferior_dir = Column(
        [estati_btn, _],
        alignment=MainAxisAlignment.CENTER,
        spacing=75
    )
    
    # Container principal
    main_container = cria_container_elementos(
        Column(
            [
                Row( # Row superior
                    [coluna_superiorA, coluna_superiorB],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=250
                ),
                Row( # Row inferior
                    [
                        coluna_inferior_esq,
                        coluna_inferior_dir
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=75
                )
            ]  
        )
    )
    main_container.margin = 20
    main_container.width = 1200
    main_container.height = 680
    
    page.add(
        Row(
            [main_container],
            alignment=MainAxisAlignment.CENTER
        )
    )
    
