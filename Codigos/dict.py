# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "CHAVE" e "VALOR".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')


pessoa = {
    "Nome" : "Augusto",
    "Sobrenome" : "Hanashiro",
    # "endereco" : {"rua": "Rua x", "N°" : "N° x"}
}
nova_Chave = "Etnia"
pessoa[nova_Chave] = "Japonesa"

# print(pessoa["Nome"])
# del pessoa[nova_Chave]


for chave in pessoa : 
    print(chave)

print()

"""
Para saber se uma chave existe em um dicionário, utilizamos a função get("nome_chave_desejada", valor caso retorne None(opcional))
"""
if pessoa.get("Etnia") is None:
    print("Chave inexistente!")
else:
    print(pessoa["Etnia"])

print("----------")

print(pessoa.keys())
print(pessoa.values())

pessoa.setdefault("Teste", 5)

for chave in pessoa : 
    print(chave)

'''
Funções de dic 
get() - para saber se temos uma chave no dicionario 
values() - retorna apenas os valores de um dicionario 
keys() - retorna as chaves do dicionario 
setdefault() - se tiver uma chave onde não ha valor, setar um valor padrão, ou criar e chave e valor
                caso a chave não existe

copy() - faz uma copia raza de um outro dic = ou seja, copia apenas os itens imutaveis do dicionario 
        item mutaveis como a lista, o copy faz a variavel apontar para a mesma lista que o dicionario copiou

Para fazer uma copia total, é preciso importar o modulo copy e utilizar o método deepcopy()

popitem() = elimina a ultima chave do dict

update(){
    "Chave" : "valor",
}
''' 