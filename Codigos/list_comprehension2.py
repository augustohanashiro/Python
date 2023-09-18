Lista_Pessoas = [
    {"Nome":"Augusto", "idade": 20},
    {"Nome":"Airton", "idade": 35},
    {"Nome":"Luciana", "idade": 18}
]

Lista_Pessoas2 = [
    {**pessoa, "idade":pessoa["idade"]+5}
    if pessoa["idade"] > 30 else {**pessoa} # if a esquerda do for = mapeamento
    for pessoa in Lista_Pessoas
]

print(Lista_Pessoas2)


lista = [
    n*2
    for n in range(20)
    if n > 10 # if de filtro
]
# Precedencia de operação, primeiro realiza o filtro(if a direita) depois 
# adiciona o elemento(if a esquerda)

print(lista)

# For dentro de for com list_comprehension
#forma comum
multiplo_for = []
for elemento in range(3):
    for i in range (3):
        multiplo_for.append((elemento,i))

print(multiplo_for)

multiplo_for2 = [
    (x,y)
    for x in range(3)
        for y in range(3)
]
print(multiplo_for2)



'''
Para entender bem sobre isso, vc tem que ter o conhecimento de empacotamento
e desempacotamento de kwargs
Toda vez que vc fizer o mapeamento de uma lista para outra, necessariamente a 
outra lista que vc mapear deve ter o mesmo numero de elementos da lista mapeada

ENTENDENDO O CÓDIGO

1° CRIANDO A LISTA 
Lista_Pessoas2 = []

2° Fazendo o mapeamento básico primeiro:
Para toda pessoa que tiver na minha lista de pessoas, copie a pessoa(no caso uma
biblioteca) com os mesmos valores na minha nova lista 
Neste caso, pegue todas as bibliotecas que tem na lista pessoas e passe para
Lista_pessoas2

Lista_Pessoas2 = [pessoa for pessoa in Lista_Pessoas] 

3° Manuseando os elementos mapeados
Lista_Pessoas2 = [pessoa for pessoa in Lista_Pessoas] 



Lista_Pessoas2 = [
    {**pessoa, "idade": pessoa["idade"] + 5}
    if pessoa["idade"] > 30 else {**pessoa}
    for pessoa in Lista_Pessoas
]

'''
