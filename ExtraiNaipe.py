def extrai_naipe(carta):
    if carta[1] == '0':
        return carta[2]
    if carta[1] == '♦' or '♥' or '♣' or '♠' :
        return carta[1]
    