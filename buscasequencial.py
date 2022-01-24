import time


def busca_sequencial(v, x):
    i = 0
    while i <= len(v) - 1:
        if v[i] == x:
            return i

        i += 1
    return - 1


vetor = list(range(0, 10000001))
print(vetor)
chave = 9977611
antes = time.time()
posicao = busca_sequencial(vetor, chave)
depois = time.time()
total = (depois - antes)*1000
if posicao >= 0:
    print(' O elemento %d foi encontrado na posição %d.' % (chave, posicao))
else:
    print('O elemento Não foi encontrado.')

print('O tempo total gasto foi : %0.2f ms.' % total)

