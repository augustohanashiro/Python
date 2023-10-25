
# # Imutáveis - str, int, float bool tuple
# # mutaveis - list and dict 
n_studants = 0
students = []

while(n_studants < 2 or n_studants > 5 ):
    n_studants = int(input("digite o numero de estudantes:"))

for elemento in range(n_studants):
    nome = input("Nome:")
    score = float(input("Nota:"))
    students.append([nome,score])


lista_scores = []
alunos_com_segunda_menor_nota = []
segunda_menor_nota = 0
for elemento in students:
    lista_scores.append(elemento[1])

lista_scores = set(lista_scores)
lista_scores = list(lista_scores)
lista_scores.sort()


segunda_menor_nota = lista_scores[1] if len(lista_scores) > 1 else  lista_scores[0]

for nome in students:
    if segunda_menor_nota in nome:
        alunos_com_segunda_menor_nota.append(nome[0])

alunos_com_segunda_menor_nota.sort()
print(alunos_com_segunda_menor_nota)

'''
Resolução proposta
# from __future__ import print_function
# score_list = {}
# for _ in range(input()):
#     name = raw_input()
#     score = float(raw_input())
#     if score in score_list:
#         score_list[score].append(name)
#     else:
#         score_list[score] = [name]
# new_list = []
# for i in score_list:
#     new_list.append([i, score_list[i]])
# new_list.sort()
# result = new_list[1][1]
# result.sort()
# print (*result, sep = "\n")

'''







    


