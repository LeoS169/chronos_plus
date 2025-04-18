from flet import Page, MainAxisAlignment, Row, app
from assets.tools.conv import cria_container_elementos


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
    
    # Container principal
    main_container = cria_container_elementos(
        None
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
    
app(pagina_diario)