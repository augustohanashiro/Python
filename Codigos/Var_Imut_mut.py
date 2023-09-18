'''
Quando temos uma variavel apontando pra outra variavel IMUTAVEL(str,bool,int,float,tuple), 
nos dizemos que nela será ATRIBUIDA o mesmo valor
Portando, apos a atribuição, se eu alterar o valor de uma, a outra permanece o mesmo valor 
'''

palavra1 = "Augusto"
palavra2 = palavra1

palavra1 = "Airton"

print(f"{palavra2=}\n{palavra1=}")

'''
Agora se eu tenho uma variavel apontando para outra variável MUTAVEL (dict ou lista)
Nos dizemos que ela ira de fato apontar para o mesmo objeto
portano, ao alterar o elemento de uma variavel, a outra passa a sofrer a mesma alteração
'''

sala1 = ["Augusto","Airton"]
sala2 = sala1

sala1[0] = "Joyce"

print(sala1,sala2,)