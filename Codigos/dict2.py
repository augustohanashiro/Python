'''
Dicionario - baseado na logica de chave e valor
chave sempre algo imutaval(str,int,float,tuple,bool)

pode ser declarada de duas formas 

dicionario = {
    "chave" : "Valor"
    "Sobrenome" : "Hanashiro"
}

ou 

dicionario = dict(chave = "valor",sobrenome = "Hanashiro")
'''


pessoa = {
    "nome": "Augusto",
    "sobrenome": "Fonseca"
}

print(pessoa["nome"])
print()
# CRUD

# Criando chaves 
pessoa["Idade"] = 26
pessoa["Estado"] = "SP"

# Deletar chave
del pessoa["Estado"]

# Editar(Update)
pessoa["Idade"] = 30

# Read
# For dentro de um dicionario
for chave in pessoa:
    print(f"Chave:{chave} Valor:{pessoa[chave]}")


# Listar as chaves
print(pessoa.keys(),type(pessoa.keys()))
# Para tornar a manipulação mais interessante, convertemos para lista ou tuple
print(tuple(pessoa.keys()))


# Listar as valores
print(pessoa.values(),type(pessoa.values()))
# Para tornar a manipulação mais interessante, convertemos para lista ou tuple
print(tuple(pessoa.values()))

# Listar os itens
print(pessoa.items(),type(pessoa.items()))
# Para tornar a manipulação mais interessante, convertemos para lista ou tuple
print(tuple(pessoa.items()))

for chave,valor in pessoa.items():
    print(chave,valor)

# metodo, caso não haja uma chave na lista, crie e atribua um valor padrao 

pessoa.setdefault("Estado_Civil","Solteiro")
print(pessoa)

# copy|shallow copy|copia raza vs deepcopy|copia profunda 

# copy|shallow copy|copia raza copia todos os itens imutaveis de uma lista, e os itens mutáveis
# serão apontados para os mesmos elementos de sua origem, ou seja, se mudar na origem, muda na copia

d1 = {
    "c1": "Valor1",
    "c2": "Valor2",
    "c3": ["Augusto,","Airton","Humberto"]
}

d2 = d1.copy()

print("\nAntes De mudar")
print("D1")
for chave,elemento in d1.items():
    print(chave,elemento)
print("D2")
for chave,elemento in d2.items():
    print(chave,elemento)
print()

d1["c3"][0] = "Airton"

print("Depois de mudar um item da lista - Repare que nos dois dicionarios ira mudar")
print("D1")
for chave,elemento in d1.items():
    print(chave,elemento)
print("D2")
for chave,elemento in d2.items():
    print(chave,elemento)
print()

# Agora no deepcopy. Todos os elementos irão ser copiados, independente de ser imutavel ou não
# Para fazer deepcopy vc deve importar o modulo copy

import copy

d2 = copy.deepcopy(d1)
print("\n------Agora com deepcopy---------")
print("\nAntes De mudar")
print("D1")
for chave,elemento in d1.items():
    print(chave,elemento)
print("D2")
for chave,elemento in d2.items():
    print(chave,elemento)
print()

d1["c3"][0] = "Teste"

print("Depois de mudar um item da lista - Com deepcopy, a copia não ira ser afetada\
se o outro elemento for atualizado")
print("D1")
for chave,elemento in d1.items():
    print(chave,elemento)
print("D2")
for chave,elemento in d2.items():
    print(chave,elemento)
print()

# Aula 

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)