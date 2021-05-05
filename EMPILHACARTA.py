
def empilha(baralho,inicio,destino):
    novo = []
    for carta in baralho:
        novo.append(carta)
    cartadeslocada = novo[inicio]
    novo[destino] = cartadeslocada
    novo.pop(inicio)
        return novo