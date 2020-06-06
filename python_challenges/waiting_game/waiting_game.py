# Criar um jogo chamado Waiting Game.
# O pc gera um target entre 2s a 4s assim que o usuário aperta start
# Então o usuário aperta enter novamente para interromper o jogo e verificar se o perído de espera foi exato ao estipulado pelo pc

import time
import random

def waiting_game():

    target = random.randint(2,4)
    print(f'\nSeu objetivo é esperar {target} segundos\n')

    input('Digite Enter para iniciar o relógio.')
    start = time.perf_counter()

    input(f'Digite Enter novamente após {target} segundos.')
    resultado = time.perf_counter()-start
    print(f'O resultado foi de {resultado} segundos')

    if resultado == target:
        print('Parabéns! Vc acertou!')
    elif resultado < target:
        print(f'Deveria esperar um pouco mais! {target - resultado} segundos a mais!')
    else:
        print(f'Esperou demais!{resultado-target} segundos a menos!!')
        
if __name__== '__main__':
    

    while True:
        print()
        print('Bem vindo ao Waiting Game')
        print()
        print('o periodo de espera é de 2s a 4s.')
        print()
        print('Pronto para o desafio?')
        print()
        start = input('Pressione Enter para começar ou exit para sair')
        if start == '':
           waiting_game()
        else:
            break