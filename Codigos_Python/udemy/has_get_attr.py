'''
hasattr -> metodo que me verifica se um objeto tem um atributo especifico

getattr -> em caso de hasattr gerar um valor verdadeiro, o getattr vai fazer
com que possamos executar o codigo 


'''

string = "Augusto"
metodo = "upper"

print(hasattr(str,"upper"))
# ou
print(hasattr(str,metodo))

if (hasattr(string,metodo)):
    print(getattr(string,metodo)())