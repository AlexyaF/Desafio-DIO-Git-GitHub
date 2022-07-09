from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
start = input('\033[1;35mPRESSIONE ENTER PARA JOGAR OS DADOS\033[m')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('AAAEIO')
print('\033[1;32mSORTEANDO.....')
sleep(1)
print('\033[1;47;30mVALORES SORTEADOS:\033[m')
ranking = list()
for k, v in jogo.items():
    sleep(0.8)
    print(f'\033[1;36m{k.upper()} TIROU {v} NO DADO\033[m')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('\033[1;47;30m  == RANKING DOS JOGADORES ==\033[m')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'\033[1;32m {i + 1}° LUGAR, {v[0].upper()} COM {v[1]}')

