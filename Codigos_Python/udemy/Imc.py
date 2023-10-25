# imc = peso/altura**2

nome = "Augusto"
peso = 95
altura = 1.80

imc = peso/altura**2

# print("O nome do paciente é {nome}\nPeso:{peso}\nAltura{altura}")
# print(imc)

teste = ("O nome do paciente é {}\nPeso:{:.1f}\nAltura{:.2f},Testando se funcionou: {teste} ").format(nome,peso,altura, teste = "funcionou")
print(teste)