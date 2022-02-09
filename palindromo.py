def palindromo(palavra):
    lista_palavra = list(palavra)
    tamanho_palavra = len(lista_palavra)
    for i in range(tamanho_palavra):
        if lista_palavra[i] != lista_palavra[tamanho_palavra - 1 - i]:
            return False

    return True


print(palindromo('mussum'))
print(palindromo('jose'))
print(palindromo('abacate'))
