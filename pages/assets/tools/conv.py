from flet import (ElevatedButton, Text, 
ButtonStyle, RoundedRectangleBorder, Container,
BoxShadow, Column, TextField, TextStyle)

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
    

def cria_container_elementos(content):
    return Container(
        content=content,
        bgcolor="#25274A",
        width=560,
        height=540,
        border_radius=30,
        padding=65,
        shadow=BoxShadow(
            spread_radius=5,
            blur_radius=100   
        )
    )
    

def cria_container_entrada(label:str, fonte:str):
    return Container(
        content=Column(
                controls=[
                    Text(label ,size=60 ,font_family=fonte),
                    TextField(
                        border_radius=10,
                        border_color="#FFFFFF",
                        text_style=TextStyle(
                            font_family="Jersey10",
                            size=40
                        )
                    )
                ]
            ),
        bgcolor="#25274A",
        width=560,
        height=140 
    )