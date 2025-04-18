from flet import Page, MainAxisAlignment, Row, Column, Text, ScrollMode, Container, app
from assets.tools.conv import cria_container_elementos, cria_botao, cria_atividade

# Dados user

lista_diarios = []

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
        f"Quantidade de diários: n°",
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
    
    # Elementos do ontainer sobreposto ao principal
    diario = cria_atividade(
        Row(
            [
                Text("1", font_family="Jersey15", size=50),
                Text("ativo", font_family="Jersey15", size=50),
                Text("Tempo total: 20h", font_family="Jersey15", size=50)
            ],
            alignment=MainAxisAlignment.CENTER,
            spacing=50
        )
    )
    
    lista_diarios.append(diario)
    
    voltar_botao = cria_botao(
        "Voltar", None
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
    
app(pagina_diario)