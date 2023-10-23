# Enunciado : https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

# A classe Counter() recebe como argumento, uma lista, e gera um dicionario
# Com os itens da lista como chaves, e suas ocorrnecias como valores 

from collections import Counter 

tenis_disponivel = input()
lista_tamanhos = Counter(map(int,input("Digite os tamanhos separado por espaços:").split(" ")))
n_clientes = int(input("N° clientes:"))
total = 0
for i in range(n_clientes):
    tamanho, valor = map(int,input("Digite o tamanho e o valor do tenis:").split(" "))
    if lista_tamanhos[tamanho] > 0:
        lista_tamanhos[tamanho]-=1
        total+=valor
    
print(total)
