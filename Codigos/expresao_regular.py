import re 

numeros = "1657saadsd98456sad4"

numeros = re.sub(
    r"[^0-9]", # quero substituir todos os valores que não sejam numeros
    "", # Quero trocar por nada, ou seja, apagar o caractece que não seja numero
    numeros # variavel que desejo estudar
)

# ^ é o valor de negação
# Expressão regular - sub(r"O que vc deseja substituir na sua string","Pelo que vc deseja
#  substituir", variavel que vc deseja aplicar o sub)
print(numeros)