nomes = ["Augusto","Humberto","Maria"]

for item in enumerate(nomes):
    print(item)


'''
'enumerate' converte todo item iteravel, em uma tupla, ou seja, uma lista imutável, com dois termos
o primeiro referindo ao indice
e o segundo referindo ao conteudo
Toda vez que utilizamos enumarete, dentro do for, vc pode utilizar um ou dois argumentos:


EXEMPLO:

nome = "Augusto"

enumerado = enumerate(nome)

for indice,conteudo in enumerado:
    print(indice, conteudo)

Neste caso, o nome passou a ser uma string com cada letra tendo um indice

************* TODA VEZ QUE VC UTILIZA O ENUMERATE, SERA CRIADO UM ITERAVEL, QUE SÓ PODE SER UTILIZADO UMA VEZ 
POR ISSO, O CODIGO ABAIXO SÓ SERA UTILIZADO UMA VEZ:

nomes = ["Augusto","Humberto","Maria"]

lista_enumerada = enumerate(nomes)

for item, nome in lista_enumerada:
    print(nome)

for item, nome in lista_enumerada:
    print(nome) 

O ideal é realizar o código como está exibido nas primeiras linhas deste arquivo
se convertemos a lista em enumerate dentro de um ciclo for, podemos utiliza-lo inumeras vezes
'''