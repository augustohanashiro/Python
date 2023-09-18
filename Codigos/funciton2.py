def soma(*args):
    print(args)
    total=0
    for elemento in args:
        print(f"{elemento} + {total} = {total + elemento} ")
        total += elemento

    print(total)

teste  = 1,2,3,4,5

soma(*teste)

'''
Quando escrevemos uma função com a definição de "*args"
Quer dizer que os argumentos que serão passados dentro da função serão juntados em uma tupla
portanto, se passarmos uma tupla, ocorrera um empacotamento de uma tupla em outra tupla, gerando erro

O correto é 
'''