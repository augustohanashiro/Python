'''
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# # s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# SETS SÃO EFICIENTES PARA REMOVER VALORES DUPLICADOS DE ITERAVEIS
# - Não aceitam valores mutáveis - LIST OU DICT; - ACEITA VALORES IMUTAVEIS - TUPLA, INT, STR, FLOAT
# - Seus valores serão sempre únicos - REMOVE VALORES DUPLICADOS;
# - não tem índexes;
# - NÃO GARANTEM A ORDEM DOS ELEMENTOS;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add - adiciona um imutavel no seu set - aceita apenas um argumento
 update - Aceita varios argumentos para adicionar, porem, se vc passar um iterável como uma string
 ele ira adcionar cada letra da sua string separadamente

 EXEMPLO:
s1 = set()

s1.update("Ovo")
print(s1)

OUTPUT:
{"O","V","O"} (Lmebrando que a ordem das letras não é garantida)

************************************************************************
Caso queria adicionar a string inteira como um elemento, basta passar no update essa string dentro
de um iteravel (list/tupla)

clear() - Limpa todo o set 

discard() -  elimina o termo que vc passar como argumento

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

'''

s1 = {1,2,3}
s1.update(
    ("teste")
)
print(s1)
# s1.add("teste")

# print(s1)
