from json import dump

"""
Esse arquivo contém funcoes
para atualização de informações
do userinfo.json
"""

def define_userinfo(
    user:tuple, # format "(a, b,)"
    qntDiario:int,
    diarioAtivo:str # nome do diario
):
    with open("pages/userinfo.json", "w") as f:
        dump(
            {
                "user": f"{user}",
                "qntDiario": qntDiario,
                "diarioAtivo": diarioAtivo
            }, f
        )
    return None