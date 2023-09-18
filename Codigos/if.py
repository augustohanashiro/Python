primeiroValor = input("Digite o primeiro valor: ")
segundoValor = input("Digite o segundo valor: ")

if primeiroValor > segundoValor: 
    print(f"Primeiro valor:{primeiroValor} é maior que o segundo valor:{segundoValor}!")
elif segundoValor > primeiroValor:
    print(f"Segundo valor:{segundoValor} é maior que o primeiro valor:{primeiroValor}!")
else: 
    print("Valores iguais")

