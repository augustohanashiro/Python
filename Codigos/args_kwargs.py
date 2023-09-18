# '''
'''
Se o *args for dado como parâmetro de uma função, ele ira empacotar todos os argumentos em uma 
tupla

Se pegarmos um iteravel como tuplas, e colocarmos em uma variavel, 
se passarmos essa variavel com um asterisco antes, nos iremos desempacotar a tupla em varios elementos
 
'''
# Lembrete: a passagem de argumentos (args) é separada por virgulas, e a de dicionarios (kwargs) 
# é separada por atribuição de valores
# kwargs é todo conjunto de elemento nomeados, que gera a formação de um dicionario :
# dicionario = dict(nome="qlqr")
# Exemplo:
# def teste(**qlqr):
#   print(qlqr, type(qlqr))
# 
# teste(nome ="Augusto")
# 

# '''
def exibir_poema(data_poema, *args,**kwargs):
    texto = "\n".join(args)
    dicio = "\n".join(f"{chave.title()}: {valor}" for chave,valor in kwargs.items())
    mensgem = f"{data_poema}\n\n{texto}\n\n{dicio}"
    print(mensgem)
exibir_poema (
    "Sexta, qlqr dia",
    "The Zen of Python, by Tim Peters",
    "Beautiful is better than ugly",
    "Explicit is better than implicit",
    "Simple is better than complex",
    "Complex is better than complicated",
    "Flat is better than nested",
    "Sparse is better than dense",
    "Readability counts",
    "Special cases aren't special enough to break the rules",
    "Although practicality beats purity",
    "Errors should never pass silently",
    "Unless explicitly silenced",
    "In the face of ambiguity, refuse the temptation to guess",
    "There should be one -- and preferably only one -- obvious way to do it",
    "Although that way may not be obvious at first unless you're Dutch",
    "Now is better than never",
    "Although never is often better than *right* now",
    "If the implementation is hard to explain, it's a bad idea",
    "If the implementation is easy to explain, it may be a good idea",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="x",
    ano = "y"
)

# def ant_suc(numero):
#     ant = numero - 1
#     suc = numero +1

#     return ant,suc

# print(ant_suc(3))

def teste (*args):
    string = []
    string.append(args)

# print(teste(5,4,6,8,4,3,5))
    