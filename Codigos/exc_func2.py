# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(a=0):
    return "par" if a % 2 == 0 else "impar" 

teste = par_impar(15)

print(teste)