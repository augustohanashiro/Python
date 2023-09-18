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
#  Miha resolção

cont_regressivo_p = 10
cont_regressivo_s = 11
digito_cpf = 0
indice_coleta = 0
# Montando lista com numeros do cpf
cpf_checagem = []
# Montando lista com numeros para checar o primeiro indice 
cpf_op_1 = []
# Montando lista com numeros para checar o segundo indice 
cpf_op_2 = []
soma = 0
soma2 = 0
resto_divisao = 0
while True:

    cpf = input("Digite o seu cpf:")
# Montagem de uma lista com os numeros do cpf coletado
    while digito_cpf < 9:
        if cpf[indice_coleta].isdigit():
            cpf_checagem.append(int((cpf[indice_coleta])))
            digito_cpf += 1
            indice_coleta += 1
        else:
            indice_coleta += 1

    cpf_op_1 = cpf_checagem.copy()

    print(cpf_checagem)

# Contagem para ver o primeiro indice do cpf:

    for indice, conteudo in enumerate(cpf_checagem):
        cpf_op_1[indice] = conteudo * cont_regressivo_p
        cont_regressivo_p -= 1
    
    print(cpf_op_1)

    for elemento in cpf_op_1:
        soma += elemento

    print(soma)

    # conferindo o primeiro digito
    soma *= 10
    resto_divisao = 0 if soma % 11 > 10 else soma % 11

    # Print do primeiro difito
    print(resto_divisao)

    # Junção dos primeiros numero do cpf ao primeiro digito
    cpf_checagem.append(resto_divisao)


    cpf_op_2 = cpf_checagem.copy()

    print(cpf_checagem)


    for indice, elemento in enumerate(cpf_checagem):
        cpf_op_2[indice] = elemento * cont_regressivo_s
        cont_regressivo_s -= 1

    print(cpf_op_2)

    for elemento in cpf_op_2:
        soma2 += elemento
    
    print(soma2)
    
    soma2 *= 10
    resto_divisao = 0 if soma2 % 11 > 10 else soma2 % 11

    # Print do primeiro difito
    print(resto_divisao)

    cpf_checagem.append(resto_divisao)

    print(cpf_checagem)


# CPF: 746.824.890-70


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
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
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
    