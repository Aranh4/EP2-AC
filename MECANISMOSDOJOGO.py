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



print (extrai_valor('A0'))

##### movimentospossiveis.py

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


###empilha carta
def empilha(baralho,inicio,destino):
    novo = []
    for carta in baralho:
        novo.append(carta)
    cartadeslocada = novo[inicio]
    novo[destino] = cartadeslocada
    novo.pop(inicio)
    return novo