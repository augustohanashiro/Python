def saudacao(a,b):
    def cumprimento():
        return print(f"{a} {b}")
    
    return cumprimento



teste = saudacao("Bom dia","Augusto") 
#  teste por baixo dos panos esta armazenado a função cumprimento 
#  teste = cumprimento

#  que por sua vez esta armazenado o print 
#  teste = print(f"{a} {b}")
#
#   portanto para executala, basta adicionar os parenteses 
teste()



# -------------------------------------------------------


def bom_periodo(periodo):
    def nome(nome):
        return f"{periodo} {nome}"
    return nome

cumprimento = bom_periodo("Boa tarde")

print(cumprimento("Augusto"))

