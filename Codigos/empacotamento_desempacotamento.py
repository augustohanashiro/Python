'''
Desempacotamento é o ato de gerar elementos iteraveis 
se for uma lista, o desempacotamento é gerar varios elementos iteraveis
se for uma string, o desempacotamento é gerar cada caractere como um elemento


Desempacotamento é o ato de atribuir varios valores a varias variaveis de uma vez só
Voce vai desempacotar as variaveis e os valores dados, e atribui-los um a um 

var1,var2,var3 = valor1,valor2,valor3 ---> var1 = valor1 | var2 = valor2 | var3 = valor3

Empacotamento é o fato de atribuir um conjunto de valores (uma lista) a uma variavel
para fazer a atribuição de vários valores a uma variavel, é preciso colocar o * antes do nome da 
variavel 

var1, *var2 = "Augusto","Airton","Humberto"

var1 = Augusto
var2 = ["Airton","Humberto"]

'''

lista = [1,2,3,4,5,6,7]
v1,v2,*elementos,u = lista

print(v1,v2)
print(v1,u)
print(elementos)


lista2 = ["Augusto","Airton","Humberto"]

for indice,elemento in enumerate(lista2):
    print(f"Elemento {indice + 1} da lista")
    for letra in elemento: 
        print(letra, end="-")
    print("\n")    

# Desempacotamento de itens como passagem de argumentos em print 

lista = "elemento1","elemento2","elemento3" #tupla

# print(*lista) = print("elemento1","elemento2","elemento3")
print("Desempacotando um iteravel")
print(*lista)

nome = "Augusto"
print("Testando desempacotamento com string")
print(*nome)
print("\n")
# Lista dentro de lista
lista_aninhada = [
    [1,2,3,4],
    [4,5,6,7],
    [9,8,7,]
]

print("Print de lista sem alterar sep:")
# Repare a diferença 
print(*lista_aninhada)
print("\n")

print("Print de lista alterando o sep:")
print(*lista_aninhada, sep="\n")

