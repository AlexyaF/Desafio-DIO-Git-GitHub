

"""
       STYLE                       TEXT/CORES DE FUNDO
    0 : sem estilo      30/40 : branco       34/44 : azul
    1 : negrito         31/41 : vermelho     35/45 : roxo
    4 : sublinhar       32/42 : verde        36/46 : azul claro
    7 : negativo        33/43 : amarelo      37/47 : cinza(padrão)
"""
print('\033[0:30:41mOlá mundo\033[m')
print('\033[4:33:44mOlá mundo\033[m')
print('\033[1:35:43mOlá mundo\033[m')
print('\033[1:30:42mOlá mundo\033[m')
print('\033[mOlá mundo\033[m')
print("\033[1:7:30mOlá mundo\033[m")
a = 3
b = 5
print(f'OS VALORES SÃO \033[1:36m{a}\033[m E \033[1:35m{b}\033[m !!!')