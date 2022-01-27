def numeros(mudar):
    for i in range(len(mudar)):
        if mudar[i] < 0:
            mudar[i] = 0
        elif mudar[i] < 10:
            mudar[i] = 1
        else:
            mudar[i] = 2

    return mudar


lis = []
for i in range(0, 8):
    numero = int(input('Digite um numero: '))
    lis.append(numero)

print(lis)
numeros(lis)
print(lis)



