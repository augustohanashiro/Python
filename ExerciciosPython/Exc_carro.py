velocidade_carro = 60
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RANGE_1 = 1


carro_acima_velocidade = velocidade_carro > RADAR_1
carro_no_range = local_carro >= LOCAL_1 - RANGE_1 and local_carro <= LOCAL_1 + RANGE_1

if carro_no_range:
    print("Carro esta no range")
    if carro_acima_velocidade:
        print("Carro Multado")
    else:
        print("Carro dentro do limite de velocidade")
else:
    print("Carro não está no range")
