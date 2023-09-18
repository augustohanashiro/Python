def soma(a,b=5):
    print(a + b)


soma(10)

'''

PARA PASSAR EM UMA FUNÇÃO UM ARGUMENTO DE VALOR PADRÃO, É UTILIZADO O VALOR NONE

soma(x,y,z=None)*********** o argumento z não precisa ser passado

Diferença entre argumento e parâmetro

parâmetro é a requisição de passagem para uma função 

argumento é o valor dos parametros passados

exp
area(base,altura) <- base e altura são parâmetros da função

área(5,2) <- 5 e 2 são os argumentos passados para o calculo da área

********* apos passar um argumento nomeado, todos os seguintes devem ser nomeados também

volume(x,y,z):
    print(x * y * z)

volume(10,y=5, 6) -> está forma está errada, pois o y é um argumento nomeado, portanto o seguinte 
                     tambem deve ser
volume(10,y=5, z=6) -> forma correta de chamar a função     


argumentos podem ser 
    -nomeados :
     soma(x=1,y=2)

    -Posicionais / Não nomeados
    soma(1,2)


COISA IMPORTANTE EM FUNÇÃO

Todo retorno de uma função é um não valor (NONE)

    Se vc passar um argumento nomeado = 0 na sua função, ela para fins de comparação/informação
    essa variável será visto como 'false'

    para evitar essa situação, e ter um valor não enviado sempre definido como none, utilizamos

    soma(a,b,c=None)

    if c is None
        print("Não Valor")


'''