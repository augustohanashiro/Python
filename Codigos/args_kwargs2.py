'''
Melhor codigo para diferenciar args e kwargs
'''

def diferenciar_args_kwargs(*args,**kwargs):
    print("Args | Parametros não nomeados | Parâmetro posicional",args, sep="\n")
    print("Kwargs | Parâmetro nomeado", kwargs, sep="\n")


diferenciar_args_kwargs(1,2,3,4,nome="Augusto",cidade = "São Paulo")


# Desempacotamento de dicionario para criação de um outro dicionario (Junção)

print("\n-----------\n")
config = {
    "c1" : 1,
    "c2" : 2,
    "c3" : 3,
    "c4" : 4
}

config2 = {
    "c5" : 5,
    "c6" : 6,
    "c7" : 7,
    "c8" : 8,

}

config3 = {
    **config,
    **config2
    }

print("Config3:")
for elemento in config3.items():
    print(elemento)