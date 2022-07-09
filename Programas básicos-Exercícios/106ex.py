from time import sleep
while True:
    print('\033[1;35;40m=' * 30)
    print('\033[1;36;40mSISTEMA DE AJUDA PyHELP')
    print('\033[1;35;40m=' * 30)
    print('\033[m')
    user = str(input('\033[1;32mFUNÇÃO OU BIBLIOTÉCA:\033[m ')).strip()
    if user.upper() in 'FIM':
        print('\033[7;31;40mPROGRAMA ENCERRADO!')
        break
    else:
        sleep(1)
        print('\033[1;30;42m=' * 40)
        print(f'ACESSANDO O MANUAL DO COMANDO {user}')
        print('=' * 40)
        print('\033[m')
        sleep(1)
        print('\033[1;47;30m')
        help(user)
        print('\033[m')
        sleep(1)

