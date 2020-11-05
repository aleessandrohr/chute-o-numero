from time import sleep
from random import randint

def leiaint(número):
    while True:
        try:
            número = int(input(f'{número}'))
        except:
            print(f'\033[31mPor favor digite um número inteiro.\033[m')
        else:
            return número


def linha(msg='', cor='\033[m', fim='\033[m'):
    print(f'{cor}-' * 42)
    print(msg.center(42))
    print(f'{cor}-{fim}' * 42)


def opção():
    while True:
        opção = leiaint('Seu chute: ')
        if opção >= 1 and opção <= 100:
            return opção
        else:
            print('\033[31mDigite uma valor válido!\033[m')


def gerador():
    linha('Gerando um número entre 1 a 100...', cor='\033[30m')
    sleep(3)
    número = randint(1, 100)
    while True:
        op = opção()
        if op > número:
            print(f'\033[31mTente um número mais baixo!\033[m')
        elif op < número:
            print(f'\033[31mTente um número mais alto!\033[m')
        else:
            print(f'\033[32mParabéns, você acertou o número {número}!\033[m')
            sleep(3)
            break