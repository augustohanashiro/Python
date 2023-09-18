# Conjunto de objetos que não se repetem e não garantem ordem

# Mesmo repetindo ao imprimir, só sera retornado elementos exclusivos
primeiro_set = {1,3,5,4,6,4,8,5,2} 

print(primeiro_set)

segundo_set = { "p","h","y","t","o","n","h","p"}

print(segundo_set)

# Podemos fazer alguns agrupamentos de conguntos 

set1 = {1,2,3}
set2 = {2,3,4}

# ------------------------------------------------
uniao1 = set1.union(set2)  
uniao2 = set1 | set2

print(uniao1,uniao2)

# ------------------------------------------------

intersecao1 = set1.intersection(set2)
intersecao2 = set1 & set2

print(intersecao1,intersecao2)

# ------------------------------------------------

