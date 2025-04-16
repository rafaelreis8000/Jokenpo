from random import choice
from time import sleep

#possibilidades que o PC pode jogar
jogadas=('PEDRA','PAPEL','TESOURA')

user = int(input(
    '\nVAMOS JOGAR PEDRA, PAPEL OU TESOURA!!!'
    '\nescolha um e veremos quem ganhou!'
    '\n\n[ 1 ] PEDRA'
    '\n[ 2 ] PAPEL'
    '\n[ 3 ] TESOURA\n\n --> '
))

escolha = '' #cria uma variável em branco

if user == 1:
    escolha = 'PEDRA'

elif user == 2:
    escolha = 'PAPEL'

elif user == 3:
    escolha = 'TESOURA'
sleep(1)
print('\nVocê escolheu {}'.format(escolha))
sleep(1)
print('\nAgora é a minha vez...')
sleep(1)
pc = choice(jogadas) #escolhe uma das opções possíveis no jogo
print('E eu escolhi...')
sleep(1)
print('\n{}!!!'.format(pc)) 

if pc == escolha:
    sleep(1)
    print('\nEscolhemos a mesma coisa!!! EMPATE!!!')

elif pc == 'PEDRA' and escolha == 'PAPEL':
    sleep(1)
    print('\nÉ... Eu perdi. Papel engole pedra!')

elif pc == 'PEDRA' and escolha == 'TESOURA':
    sleep(1)
    print('\nPedra quebra tesoura, então eu ganhei!!!')

elif pc == 'PAPEL' and escolha == 'PEDRA':
    sleep(1)
    print('\nPapel embrulha pedra, então eu ganhei!!!')

elif pc == 'PAPEL' and escolha == 'TESOURA':
    sleep(1)
    print('\nÉ... Eu perdi. Tesoura corta papel!')

elif pc == 'TESOURA' and escolha == 'PEDRA':
    sleep(1)
    print('\nÉ... Eu perdi. Pedra quebra tesoura!')

elif pc == 'TESOURA' and escolha == 'PAPEL':
    sleep(1)
    print('\nTesoura corta papel, então eu ganhei!!!')