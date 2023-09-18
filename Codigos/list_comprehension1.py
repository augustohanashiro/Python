# List comprehention é a forma de criar listas a partir de iteraveis

# Forma normal de criarmos uma lista
lista = [1,2,3]
print(lista)

# OU

lista1= list(range(9))
print(lista1)
# OU

lista2 = []
for elemento in range(9):
    lista2.append(elemento)
print(lista2,"\n")

# Forma de list_comprehention - criando listas a partir dos iteraveis 

lista_comprehension = [elemento for elemento in range(9)]
print("list Comprehension",lista_comprehension, sep="\n")

# podemos operar no valor passado antes do form tambem

lista_comprehension2 = [elemento * 2 for elemento in range(9)]
print("list Comprehension 2:",lista_comprehension2, sep="\n")
