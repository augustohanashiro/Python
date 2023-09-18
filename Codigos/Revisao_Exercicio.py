"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

while True:
    cpf = input("Digite um cpf:")
    contador_regressivo_1 = 10
    soma_Digit_1 = 0
    primeiro_digito = 0


    while(len(cpf) > 9):
        cpf = input("Digite um cpf:")

    for indice, numero in enumerate(cpf):
        while indice < 9:
            soma_Digit_1 = soma_Digit_1 + int(numero)* contador_regressivo_1
            contador_regressivo_1-=1
            break
    
    soma_Digit_1 *= 10
    primeiro_digito = soma_Digit_1%11

    if primeiro_digito > 9:
        primeiro_digito = 0
   

    print("Primeiro digito é: ", primeiro_digito)

        
    '''
    Calculo do segundo dígito do CPF
    CPF: 746.824.890-70
    Colete a soma dos 9 primeiros dígitos do CPF,
    MAIS O PRIMEIRO DIGITO,
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 11

    Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

    Somar todos os resultados:
    77+40+54+64+14+24+40+36+0+14 = 363
    Multiplicar o resultado anterior por 10
    363 * 10 = 3630
    Obter o resto da divisão da conta anterior por 11
    3630 % 11 = 0
    Se o resultado anterior for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta

    O segundo dígito do CPF é 0

    '''
    soma_Digit_2 = 0
    contador_regressivo_2 = 11
    cpf += str(primeiro_digito)
    for elemento in cpf:
        soma_Digit_2 = soma_Digit_2 + int(elemento)*contador_regressivo_2
        contador_regressivo_2 -= 1
        
    soma_Digit_2 *=10
    print("Segundo digito é:", soma_Digit_2 % 11 if soma_Digit_2 % 11 <=9 else 0  )

    
    
