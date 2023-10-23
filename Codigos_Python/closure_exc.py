# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(numero):
    def multiplicar(a):
        return f"{numero*a}"
    return multiplicar

teste = criar_multiplicador(5)

print(teste(6))