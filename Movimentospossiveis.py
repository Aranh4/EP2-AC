def extrai_naipe(carta):
    if carta[1] == '0':
        return carta[2]
    if carta[1] == '♦' or '♥' or '♣' or '♠' :
        return carta[1]
    

def extrai_valor(carta):
    if carta[1]=='0':
        return carta[0] + carta[1]
    if carta[1] != '♦' or '♥' or '♣' or '♠':
        return carta[0]


def lista_movimentos_possiveis(baralho,i):
    movimentos = []
    if i == 0:
        return movimentos
    elif i == 1 or i==2:
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]):
            movimentos.append(1)
        return movimentos
    elif i==3 or i==4:
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]):
            movimentos.append(1)
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]):
            movimentos.append(3)
        return movimentos
    elif i>4:
        return movimentos