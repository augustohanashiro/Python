
# Todo objeto iteravel, possui um atributo chamado iterador 
lista = "Augusto","Airton","Humberto"
iterador = lista.__iter__()
iterador = iter(lista)#essa linha e a de cima fazem a mesma coisa

# O iterador tem a unica responsabilidade de fornecer qual o proximo item 
# do seu conjunto com o metodo next(), podendo ser chamado de duas formas:
 
print(iterador.__next__())
# OU
print(next(iterador))
