# Link Exercicios:
# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true


# Minha Resolução:
# string = "123456"
# k = 2  #Numero de caracteres que ira ter cada item da minha lista
# lista = []
# lista_final = []
# contador_string = 0
# while contador_string < len(string):
#     contador_letra = 0
#     item = ""
#     while contador_letra < k:
#         item += string[contador_string]
#         contador_letra+=1   
#         contador_string +=1
#     lista.append(item)

# for item in lista:
#     letras = ""
#     for letra in item:
#         if letra not in letras:
#             letras += letra
#     lista_final.append(letras)
#     ...
# ------------------------------------------------------------
# Gabarito
# s = input().strip()
# k = int(input())
# i = 0
# while i < len(s):
#     a = s[i:i+k]
#     output = ""
#     for x in a:
#         if x not in output:
#             output += x
#     print (output)
#     i += k