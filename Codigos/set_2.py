'''
Operadores importantes com set 
 | - união de sets 
 & - intersecção
 "-" = diferença ( do set a esquerda, tirar os valores do set a direita) A ordem interfere o resultado
 ^ - diferença simétrica ( retornar tudo que não tem em comum nos dois sets ) ou seja, todos os valores
 fora da intersecção 
 LEMBRETE - O SETS RETORNÃO APENAS VALORES EXCLUSIVOS, OU SEJA, NÃO TRAS VALORES REPETIDOS 
 SETS TAMBÉM NÃO GARANTEM ORDEM DE PARÂMETROS, JUSTAMENTE POR ISSO NÃO POSSUI INDICE
'''


s1 = {1,2,3}
s2 = {2,3,4}

# {1,2,3} + {2,3,4} = {1,2,3,4}
print(s1 | s2, "União de sets")

# {1,2,3} & {2,3,4} = {2,3}
print(s1 & s2, "Intersercção de sets")

# {1,2,3} - {2,3,4} = {1}
print(s1 - s2, "difereça de set de sets")

# {2,3,4} -{1,2,3}  = {4}
print(s2 - s1, "difereça de set de sets")

# {1,2,3} - {2,3,4} - {1,4}
print(s1 ^ s2, "diferença exclusiva de sets")