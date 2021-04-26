#### CRIABARALHO.PY
#Bibliotecas
import random

#Código
def cria_baralho():
    espadas = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
    copas = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥']
    ouros = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
    paus = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    baralho = espadas + ouros + paus + copas
    random.shuffle(baralho)
    return (baralho)

#### EXTRAIVALOR.PY
def extrai_valor(carta):
    if carta[1]=='0':
        return carta[0] + carta[1]
    if carta[1] != '♦' or '♥' or '♣' or '♠':
        return carta[0]

#### EXTRAINAIPE.PY
def extrai_naipe(carta):
    if carta[1] == '0':
        return carta[2]
    if carta[1] == '♦' or '♥' or '♣' or '♠' :
        return carta[1]