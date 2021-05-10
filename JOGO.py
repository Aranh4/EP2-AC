from MECANISMOSDOJOGO import *

#TELA INICIAL

print(' ')
print('Paciência Acordeão')
print('==================')
print(' ')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo do jogo é colocar todas as cartas em \numa mesma pilha.')
print(' ')
print('Existem apenas dois movimentos possíveis:')
print(' ')
print('1. Empilhar uma carta sobre a carta imediatamente anterior;')
print('2. Empilhar uma carta sobra a terceira carta anterior.')
print(' ')
print('Para que um movimento possa ser realizado, basta que uma das duas condições \nabaixo seja atendida:')
print(' ')
print('1. As duas cartas possuem o mesmo valor ou')
print('2. As duas cartas possuem o mesmo naipe.')
print(' ')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode \nser movimentada.')
print(' ')
input('Pressione [Enter] para iniciar o jogo...')
print(' ')

#MOSTRANDO O BARALHO
print('O estado atual do baralho é:')
baralho = cria_baralho()

while True:
    j = 1
    for carta in baralho:
        print('{0}. {1}'.format(j, carta))
        j += 1
    print(' ')

    #PERGUNTANDO QUAL CARTA QUER MEXER

    if possui_movimentos_possiveis(baralho):
        while True:
            numerovalido = False
            while not numerovalido:
                numeroescolhido = int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho)))) 
                if numeroescolhido > len(baralho) or numeroescolhido < 1:
                    print('Número inválido, escolha outro válido (entre 1 a {}): '.format(len(baralho)))
                else:
                    numerovalido = True
            indexcarta = numeroescolhido-1
            #VERIFICANDO MOVIMENTOS POSSIVEIS
            movpos = lista_movimentos_possiveis(baralho,indexcarta)
            if 1 in movpos or 3 in movpos:
                if movpos == [1,3]:
                    print('Há dois movimentos possíveis: ')
                    print('1.{}'.format(baralho[indexcarta-1]))
                    print('2.{}'.format(baralho[indexcarta-3]))
