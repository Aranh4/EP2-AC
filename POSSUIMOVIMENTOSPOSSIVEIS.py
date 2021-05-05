def possui_movimentos_possiveis(baralho):
    for i in range(len(baralho)-1):
        if lista_movimentos_possiveis(baralho,i) != []:
            return True
    return False