from flet import (ElevatedButton, Text, 
ButtonStyle, RoundedRectangleBorder)

def cria_botao(texto:str, funcao):
    return ElevatedButton(
        content=Text(
            texto,
            font_family="Jersey15",
            size=60
        ),
        style=ButtonStyle(
            bgcolor="#222333",
            color="white",
            shape=RoundedRectangleBorder(radius=12),
            elevation=5,
            overlay_color="#2C2E51"
        ),
        width=400,
         height=120,
         on_click=funcao
    )