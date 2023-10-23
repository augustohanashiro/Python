'''
try, except, else, finally

try nunca pode vir sozinho
'''
# numero = input("Digite um numero:")

# try:
#     numero_float = int(numero)
#     print(f"O dobro de {numero} é {numero_float*2}")
# except:
#     print("A informação digitada não é um número")

try:
    # erro 1
    # a = 1
    # b = 0
    # a/b

    # erro 2 
    # a = b

    # erro 3
    # lista = [1,2,3]
    # print(lista["a"])
    ...
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError - Provavelmente alguma variavel no código não foi declarada")
except TypeError:
    print("TypeError - Passagem de parâmetro para função provavelmente está errado")


'''
forma de indentificar um erro
nomeia a EXCEPTION com um nome qualquer
basta acessar o atributo da instancia por meio de ponto
Exemplo

Exceotion as a 
a.__class__.__name__
'''

try:
    # a/b
    ...
except Exception as a:
    print(a.__class__.__name__)


# finnaly é o pedaço do código que sempre será executado independente de 
# haver ou não erro

try:
    8/0
except:
    print("Deu erro")
else:
    print("Operação realizada sem erro algum")
finally:
    print("Chegou aqui")
    ...
