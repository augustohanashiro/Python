'''
Crie um algoritmo que realize a multiplicação, utilizando função dentro de função
'''

def multiplicacao(numero):
    def multiplicador(multiplicador):
        return numero * multiplicador
    return multiplicador


multiplicar = multiplicacao(5)
print(multiplicar(2))