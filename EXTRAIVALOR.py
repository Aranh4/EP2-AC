def extrai_valor(carta):
    if carta[1]=='0':
        return carta[0] + carta[1]
    if carta[1] != '♦' or '♥' or '♣' or '♠':
        return carta[0]
