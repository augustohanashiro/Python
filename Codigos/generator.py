'''
generator - é uma função que executa e pausa a todo momento 
similar ao iterator -  ela so sabe informar o proximo valor do seu iteravel 
diferente de algo como uma lista, ele nao tem len ou indice, apenas retorna 
um valor na medida que vai passando pelo conjunto
parece com list comprehention para criar 
mas no lugar de [] vai ()
'''

generator = (n for n in range(5))

for i in range(10):
    try:
        print(next(generator))
    except(StopIteration):
        print("iterador chegou ao fim")

'''
introdução a funções do generator

dentro de uma função normal, comumente utilizamos a palavra return para 
terminar uma função e retornar um valor qlqr 

porém o generetor, sempre executa uma função, retorna um valor e seu processamento
é pausado, conforme vamos avançando com o iterador, minha função só se encerrara
com a execução do meu ultimo item iteravel
para uma função generator pausar, utiliazmos a palavra yield
'''
print("\n-------------------------------\n")

def generation():
    print("Primeiro yield")
    yield 1
    print("Segundo yield")
    yield 2
    print("Acabou")
    return "fim"

teste = generation()
print(next(teste))
print(next(teste))
# print(next(teste)) essa ultima chamada vai gerar erro no codigo de stopiteration

print("\n-------------------------------\n")


def generator(n=0, max=10):
    while n <= max:
        yield n
        n+=1
        

gen = generator()
print("primeiro next",next(gen))
print("Segundo next",next(gen))

# for abaixo, é o "consumo do iteravel" com o next 
for n in gen:
    print(n)

print("\n--------------------\n")

def segundoGenerator(n=0, max=10):
    while True:
        if n>=max:
            return
        
        yield n
        n += 1 #Se meu código terminar aqui, ficará no loop infinito de execução

        

gen2 = segundoGenerator()
for iteravel in gen2:
    print(iteravel)



