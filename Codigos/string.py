'''
3 modos de printar algo na tela utilizando as variaveis - interpolação
'''

nome = "Augusto"

idade = 26

# Primeiro modo - % - old style

print("Ola. Meu nome é %s, tenho %d anos." %(nome,idade))

# Segundo módulo - format

print("Ola. Meu nome é {}, tenho {} anos.".format(nome,idade))
# OBS ---  não é necessário colocar na ordem, vc pode colocar os argumentos no format, e passar
# os indices começando do 0 em que cada elemento se encontra
print("Ola. Meu nome é {1}, tenho {0} anos.".format(idade,nome))



# Terceiro módulo - f strings

print(f"Ola. Meu nome é {nome}, tenho {idade} anos.")










