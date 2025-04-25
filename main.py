from os import system
from time import sleep
from random import choice

while True:
    system('cls')

    tela_inicial = input(
        '{}\n       \033[36mJOKENPO!\033[0m'
        '\n\n     \033[33m[ 1 ] JOGAR'

        '\n     [ 2 ] SAIR\033[0m\n\n{}'
        '\n \033[35m-->\033[0m '
        .format('='*22 , '='*22)
    )






    if tela_inicial == '1': #se escolher jogar

        escolha = ''
        jogadas = ('PEDRA' , 'PAPEL' , 'TESOURA')
        pc = choice(jogadas)

        while True:
            sleep(0.2)
            system('cls')

            tela_escolha = input (
                '{}\n       \033[36mESCOLHA!\033[0m'
                '\n\n     \033[33m[ 1 ] PEDRA'
                '\n     [ 2 ] PAPEL'
                '\n     [ 3 ] TESOURA\033[0m\n{}'
                '\n \033[35m-->\033[0m '
                .format('='*22 , '='*22)
            )

            if tela_escolha =='1':
                escolha == 'PEDRA'
                break

            elif tela_escolha == '2':
                escolha == 'PAPEL'
                break

            elif tela_escolha == '3':
                escolha == 'TESOURA'
                break

        sleep(0.2)
        system('cls')
        print()
        





    elif tela_inicial == '2': #se escolher sair
        sleep(0.2)
        system('cls')

        fechar_jogo = input(
            '{}\n       \033[36mSAIR?\033[0m'
            '\n\n     \033[33m[ 1 ] SIM'
            '\n     [ 2 ] NÃO\033[0m\n\n{}'
            '\n  \033[35m-->\033[0m '
            .format('='*22 , '='*22)
        )

        if fechar_jogo == '1':
            sleep(0.2)
            system('cls')
            print('{}\n        \033[31mSAINDO...\033[0m\n{}'.format('='*25 , '='*25))
            sleep(1)
            system('cls')
            break

        elif fechar_jogo == '2':
            sleep(0.2)
            system('cls')
            continue