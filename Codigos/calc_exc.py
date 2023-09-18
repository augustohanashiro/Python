while True:

    numero1 = input("Digite o primeiro numero: ")
    operador = input("Digite o operador desejado [+-/*]: ")
    numero2 = input("Digite o segundo numero: ")

    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        if operador not in "+*/-" or len(operador)>1 or not operador:
            print("Operador invalido")
            continue
        elif operador == "+":
            print("O seu resultado é:",numero1_float + numero2_float)

        elif operador == "-":
            print("O seu resultado é:",numero1_float - numero2_float)

        elif operador == "*":
            print("O seu resultado é:",numero1_float * numero2_float)

        elif operador == "/":
            print("O seu resultado é:",numero1_float / numero2_float)


    except:
        print("Um ou ambos os números não são validos")
        continue

    sair = input("Deseja sair da Calculadora? [S/N]").lower().startswith("s")
    if sair:
        break