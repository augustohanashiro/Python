numero = input("Digite um numero:")

try:
    numero_float = int(numero)
    print(f"O dobro de {numero} é {numero_float*2}")
except:
    print("A informação digitada não é um número")