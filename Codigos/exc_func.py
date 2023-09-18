# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    total = 1

    for elemento in args:
        total *= elemento
    
    return total

teste = mult(3,3,2)

print(teste)


