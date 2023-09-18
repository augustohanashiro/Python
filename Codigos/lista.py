teste_lista = ['teste', 'Augusto']
teste_lista.append(15)
teste_lista.insert(0,45)
# print(teste_lista[0],type(teste_lista[0]))
print(teste_lista)
teste_lista.sort()
print(teste_lista)

print("----------------------------------")


# outro  exercicio


lista = ["Augusto","Humberto","Maria"]

indice = range(len(lista))


print("____________________________")

for i in indice:
    print(i, lista[i])


'''
pop - se não passar argumentos, remove o ultimo elemento da lista
insert - dois argumentos( primeiro é a posição que deseja inserir, depois o valor)
append -  insere elementos na ultima posição de uma lista

Lembre que lista é um elemento mutavel 



Como colocar indices nos elementos da lista:

teste_lista = ['teste', 'Augusto']

indice = range(len(teste_lista))

for indice in indice:
    print(indice, teste_lista[indice])



PARA EMPACOTAR ELEMENTOS DE UMA LISTA:

# nome =  ["teste","Mais um teste","OUtro teste"]

nome1,*_ = ["teste","Mais um teste","OUtro teste"]



'''
