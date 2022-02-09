from random import randint
computador = randint(0, 100)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 100.')
print('Será que você consegue advinhar qual é?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez!!!')
        else:
            print('Menos...Tente mais uma vez!!!')
print('Parabéns você acertou com {} palpites!'.format(palpites))

