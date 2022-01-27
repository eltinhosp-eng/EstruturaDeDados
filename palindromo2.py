def palindromo2(palavra):
    lista_palavra = list(palavra)
    lista_invertida = list(palavra)
    lista_invertida.reverse()
    if lista_palavra == lista_invertida:
        return True
    else:
        return False


print(palindromo2('mussum'))
print(palindromo2('jose'))
print(palindromo2('abacate'))
