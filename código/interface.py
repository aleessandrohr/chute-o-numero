from PySimpleGUI import *
from random import randint
from time import sleep

valor = randint(1, 100)
change_look_and_feel('Default1')
layout = [
    [Text('Digite um número entre 1 a 100.')],
    [Input(size=(30,0), key='chute')],
    [Button('Chutar'), Button('Sair')],
    [Output(size=(30,10))] ]
janela = Window('Chute o número').layout(layout)

while True:
    event, values = janela.read()
    try:
        chuten = int(values['chute'])
    except:
        print('-' * 52)
        print('Digite um valor.')
        print('-' * 52)
    else:
        if event == 'Chutar':
            print('-' * 52)
            if chuten < valor:
                print('Tente um valor mais alto.')
            elif chuten > valor:
                print('Tente um valor mais baixo.')
            else:
                print('Parabéns, você acertou o número.')
                print('-' * 52)
                sleep(3)
                break
            print('-' * 52)

    if event == WIN_CLOSED or event == 'Sair':
        break

janela.close()