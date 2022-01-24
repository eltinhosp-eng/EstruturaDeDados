import time


def busca_binaria(lista, item):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        elemento = lista[meio]

        if elemento < item:
            primeiro = meio + 1

        elif elemento > item:
            ultimo = meio - 1

        else:
            return meio


vetor = list(range(0, 10000001))
print(vetor)
chave = 10000000
antes = time.time()
posicao = busca_binaria(vetor, chave)
depois = time.time()
total = (depois - antes) * 1000
if posicao >= 0:
    print(' O elemento %d foi encontrado na posição %d.' % (chave, posicao))
else:
    print('O elemento Não foi encontrado.')

print('O tempo total gasto foi : %0.2f ms.' % total)
