# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multipica(*args):
    total = 1
    for elemento in args:
        total*=elemento

    return total

teste_multiplica = multipica(5,5,4)

print(teste_multiplica)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def impar_par(a):
    return a%2 == 0

print("Par" if impar_par(teste_multiplica) == True else "Impar")
    
#                              OU

def par_impar(a):
    par = a % 2 == 0

    if par :
        return f"{a} é par!"
    else:
        return f"{a} é impar!"
    
print(par_impar(teste_multiplica))
