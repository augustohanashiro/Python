# listaqualquer.append(Elemento que deseja add) -> junta um objeto a lista
# listaqualquer.clear() -> Limpa a lista
# listaqualquer.copy() -> retorna a cópia de  uma lista
# listaqualquer.count(Elemento que deseja contar) -> retorna o numero de vezes que um iteravel apareceu na minha lista
# listaqualquer.extend("Primeiro elemento","Segundo elemento"...) -> junta varios elementos a uma lista
# listaqualquer.index(argumento desejado) -> retorna o indice que o argumento passado se encontra na lista
# # listaqualquer.pop() -> Exclui o ultimo elemento da lista, caso não passe a posição como argumento
# #                     caso passe a posição, excluira o elemento da posição dita (lembre que a contagem começa do 0)
# listaqualquer.remove("argumento") -> Retira a primeira ocorrencia do elemento passado 
# listaqualquer.copy() -> retorna a cópia de  uma lista
# listaqualquer.reverse() -> inverte os elementos da lista
# listaqualquer.sort() -> ordena a lista alfabeticamente
# listaqualquer.sort(reverse = True) -> ordena a lista ao contrario
# listaqualquer.sort(key = lambda x: len(x)) -> ordena a lista pelo tamanho da String 
# listaqualquer.sort(key = lambda x: len(x), reverse = True) -> ordena a lista pelo tamanho da String 
# sorted(listaqualquer, key = lambda x: len(x)) - mesma ordena

numPedidos = int(input())
contador = 1
mensagem = ""
while(contador <= numPedidos):
    prato = input()
    calorias = int(input())
    ehVegano = input()
    ehVegano = "(Vegano)" if ehVegano == "s" else "(Nao-vegano)"
    mensagem+=f"Pedido {contador}: {prato} {ehVegano} - {calorias} calorias\n"
    contador+=1
    
print(mensagem)