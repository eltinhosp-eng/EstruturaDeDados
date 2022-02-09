"""Números de Armstrong

Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.

Veja um exemplo com um número de 3 dígitos em base 10:

153 = 1^3 + 5^3 + 3^3 =  1 + 125 + 27 = 153

Problema proposto:

Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos."""


def arms():
    for n in range(1, 999999):
        calcular(n)


def calcular(n):
    # "tamanho" do n (quantos dígitos)
    # cada dígito e fazer a conta
    n_texto = str(n)
    lista_n = list(n_texto)
    numero = len(n_texto)
    soma = 0
    for i in lista_n:
        soma = int(i) ** numero + soma
    if soma == n:
        print(n)


arms()
