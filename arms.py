def arms():
    for n in range(1, 999999):
        calcular(n)


def calcular(n):
    # 153 = 1^3 + 5^3 + 3^3 =  1 + 125 + 27 = 153
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
