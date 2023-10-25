'''
Formas de importar modulos, bibliotecas

import nome_biblioteca_modulo as apelido(opcional)

from biblioteca import modulo as apelido
from biblioteca import modulo1 as apelido,


# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__ (módulo em que se encontra)
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
sys.path retorna uma lista de string com os endereços onde a IDE ira procurar os 
módulos importados 

'''
import sys

print(*sys.path, sep="\n")
