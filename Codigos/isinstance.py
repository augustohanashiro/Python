'''
 isinstance serve para saber se o objeto é de determinado tipo
'''


lista = ['A',1,1.6,[1,2,3],(1,2),{1,2},{"nome":"Augusto"}]
#        str int float list , tuple, set , dict

for elemento in lista:
    print(elemento,isinstance(elemento,str))

isinstance(elemento, (str,int)) # saber se o objeto selecionado é str OU int 


