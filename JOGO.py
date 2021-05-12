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


jogar = "S"
#CRIANDO O BARALHO
while jogar == "S":
    print('===========================')
    print('O estado atual do baralho é:')
    print('===========================')
    print('')
    baralho = cria_baralho()
    #PRINTANDO O BARALHO
    while True:
        j = 1
        for carta in baralho:
            if "♣" in carta:
                print("{}. \033[30m{}\033[0;0m ".format(j,carta))
            if "♠" in carta:
                print("{}. \033[30m{}\033[0;0m ".format(j,carta))
            if "♥" in carta:
                print("{}. \033[31m{}\033[0;0m ".format(j,carta))
            if "♦" in carta:
                print("{}. \033[31m{}\033[0;0m ".format(j,carta))
            j += 1
        print(' ')
        #VERIFICANDO SE POSSUI MOVIMENTOS POSSIVEIS
        if possui_movimentos_possiveis(baralho):
            #PERGUNTANDO QUAL CARTA GOSTARIA DE MEXER
            while True:
                numerovalido = False
                while not numerovalido:
                    numeroescolhido = int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))
                    if numeroescolhido > len(baralho) or numeroescolhido < 1:
                        print('Número inválido, escolha outro válido (entre 1 a {}): '.format(len(baralho)))
                        print('')
                    else:
                        numerovalido = True
                indexcarta = numeroescolhido-1
                #VERIFICANDO SE HA MOVIMENTOS POSSIVEIS NAQUELA CARTA
                movpos = lista_movimentos_possiveis(baralho,indexcarta)
                if 1 in movpos or 3 in movpos:
                    if movpos == [1,3]:
                        print('Há dois movimentos possíveis: ')
                        print('1.{}'.format(baralho[indexcarta-1]))
                        print('2.{}'.format(baralho[indexcarta-3]))
                        print('')
                        #ESCOLHENDO AONDE GOSTARIA DE EMPILHAR A CARTA
                        while True:
                            destino = int(input('Sobre qual carta você que empilhar o {} (1 ou 2): '.format(baralho[indexcarta])))
                            if destino != 1 and destino != 2:
                                print('Numero Inválido, escolha novamente.')
                                print('')
                                pass
                            #EMPILHANDO A CARTA  COM 2 DESTINOS AONDE GOSTARIA 
                            elif destino == 1:
                                print('Empilhando {} em {}'.format(baralho[indexcarta], baralho[indexcarta-1]))
                                print('')
                                baralho = empilha(baralho,indexcarta, indexcarta-1)
                                break
                            elif destino == 2:
                                print('Empilhando {} em {}'.format(baralho[indexcarta], baralho[indexcarta-3]))
                                print('')
                                baralho = empilha(baralho,indexcarta,indexcarta-3)
                                break
                    #EMPILHANDO A CARTA COM APENAS 1 DESTINO        
                    elif movpos == [1]:
                        print('Empilhando {} em {}'.format(baralho[indexcarta], baralho[indexcarta-1]))
                        print('')
                        baralho = empilha(baralho,indexcarta, indexcarta-1)
                    elif movpos == [3]:
                        print('Empilhando {} em {}'.format(baralho[indexcarta], baralho[indexcarta-3]))
                        print('')
                        baralho = empilha(baralho,indexcarta,indexcarta-3)
                    break
                #CONSIDERANDO QUANDO NÃO HÁ MOVIMENTOS POSSIVEIS
                else:
                    print('A carta {} não possui movimentos possiveis, selecione outra carta!'.format(baralho[numeroescolhido-1]))
                    print('')
                    pass
            pass
        #MOSTRANDO SE GANHOU OU NÃO
        else:
            if len(baralho)==2 and extrai_naipe(baralho[0]) == extrai_naipe(baralho[1]):
                baralho = empilha(baralho, indexcarta, indexcarta-1)
                print(baralho)
                print("======================")
                print('')
                print('Parabéns! Você Ganhou!')
                print("")
                print('======================')
            elif len(baralho)==2 and extrai_valor(baralho[0]) == extrai_valor(baralho[1]):
                baralho = empilha(baralho, indexcarta, indexcarta-1)
                print(baralho)
                print("======================")
                print('')
                print('Parabéns! Você Ganhou!')
                print("")
                print('======================')
            elif len(baralho)==1:
                print(baralho)
                print("======================")
                print('')
                print('Parabéns! Você Ganhou!')
                print("")
                print('======================')
            else:
                print("======================================")
                print('')
                print("Não existem mais movimentos possíveis")
                print('           VOCÊ PERDEU! ')
                print('')
                print('=======================================')
            break
    #PERGUNTANDO SE GOSTARIA DE JOGAR DE NOVO
    print('')
    continuar = True
    while continuar:
        jogar = str(input("Deseja jogar novamente? ESCREVA ESTRITAMENTE 'S' PARA 'SIM' OU 'N' PARA 'NÃO' [S/N]: "))
        if jogar != 'S' or jogar != 'N':
            print('Insira uma opção válida. [S/N]')
            print('')
            continuar = True
        if jogar == 'S':
            continuar = False
        if jogar == 'N':
            continuar = False
    print('')
    print('=========================================================================================')
print("Obrigado por jogar!")
print('Feito por: Arthur Fonseca e Caio Tieri')
print('1° Semestre - Turma A - Insper - 2021')
print('========================================')
