import ExtraiNaipe
import EXTRAIVALOR


def lista_movimentos_possiveis(baralho,i):
    movimentos = []
    if i == 0:
        return movimentos
    if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]):
            movimentos.append(1)
    if i>=3:
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]):
            movimentos.append(3)
    return movimentos