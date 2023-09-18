testando = input("Digite uma palavra")

if("a" in testando):
    print("tem 'A'")
else:
    print("Não tem 'A'")

# -------------------------------------------- prte de baixo - Interpolação de string

nome1 = "Augusto"
nome2 = "Airton"

print("%s e %s" %(nome1, nome2))
print(nome2[2])
print(nome2[-1])