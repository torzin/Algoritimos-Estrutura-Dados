def binary_search(list, n):
    first = 0 # index de inicio da lista na qual vc quer procurar n
    last = len(list) - 1 # index final da lista q vc quer procurar n
    while last >= first: 
        mid = (first + last) // 2
        if list[mid] == n:
            return True
        if n < list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

from bisect import bisect_left # módulo do python para utilizar 
                               # busca binária

sorted_fruits = ['apple', 'banana', 'orange', 'plum']
print(bisect_left(sorted_fruits, 'banana'))

# caso chame `bisect_left` e o item não exista retorna onde ele estaria
# se existisse na lista

## Desafio
# dada uma lista de palavras em ordem alfabética, escreva uma função
# que execute a busca binária de uma palavra e retorn se ela está na 
# lista
from bisect import bisect_left

def word_binary_search(word_list, word):
    idx = bisect_left(word_list, word)
    if idx <= len(word_list) - 1 and word_list[idx] == word:
        return True
    return False