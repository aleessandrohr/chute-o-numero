from interface import *
from random import randint
from time import sleep

gerador()
while True:
    while True:
        opc = str(input('Deseja sortear mais números? [S/N] ')).strip().upper()
        if opc in 'SN':
            break
        print(f'\033[31mDigite S para sim e N para não.\033[m')
    if opc == 'S':
        gerador()
    if opc == 'N':
        break
        
linha('FINALIZANDO PROGAMA...', cor='\033[31m')
sleep(3)

