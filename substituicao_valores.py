# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 30 posições.
# Testar com 4 posições, depois aumenta
# Crie uma função que recebe o vetor preenchido e substitua todas as #ocorrência
# de valores positivos por 1 e todos os valores negativos por 0

# [4, -2, 0, 1]


def numeros(namelist):
    for i in range(len(namelist)):
        if namelist[i] < 0:
            namelist[i] = 0
        else:
            namelist[i] = 1


lista = []
for i in range(0, 4):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

print(lista)
numeros(lista)
print(lista)
