# Crie um programa que escolhe uma palavra de mais de 6 letras, a partir de um texto qualquer de várias linhas,
# e pede ao usuário cada uma das letras até formar a palavra, permitindo um máximo de 8 erros.

def advinha_palavras(palavra):
  erros = 0
  original = palavra
  while erros != 3 and original != '':
    letra = str(input('Digite uma letra: '))
    if letra in palavra:
      print(letra)
      original = original.replace(letra, '')
    else:
      erros += 1
      print('Você errou, digite outra letra.')


advinha_palavras('tubarao')