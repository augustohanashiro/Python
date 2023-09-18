# função dentro de funçã


# def cumprimento(periodo):
#     def nome(nome):
#         return f"{periodo} {nome}"
#     return nome

# Bom_dia = cumprimento("Bom dia")

# Boa_tarde = cumprimento("Boa tarde")

# Boa_noite = cumprimento("Boa noite")

# print(Bom_dia("Augusto"))

def teste(**qlqr):
    for  elemento in qlqr.items():
        print(elemento, type(elemento))

teste(nome ="Augusto",idade = 26)