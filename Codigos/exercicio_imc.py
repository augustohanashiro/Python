# calculo de imc = peso(kg)/altura x altura

nome = "Augusto"
altura = 1.80
peso = 95.0

imc = peso/(altura*altura)
# imc = peso/altura**2

frase2 = "Modo 5\n{} tem  {} de altura \nE pesa {:.2f} Kg\n".format(nome,altura,peso)

#modo1
print("Modo 1\nAugusto tem " + str(altura) + " de altura\nE tem " + str(peso) + "Kg\n")

#modo2
frase = f"Modo 2\n{nome} tem  {altura} de altura \nE pesa  {peso} Kg\n"
print(frase)

#modo3
print("Modo 3\nAugusto tem",altura,"de altura\nE tem ",peso,"Kg\n")

#modo4
print(f"Modo 4\n{nome} tem  {altura} de altura \nE pesa {peso:.2f} Kg\n")

#modo5
print(frase2)



