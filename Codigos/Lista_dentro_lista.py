# Lista aninhada

salas = [
    ["helena", "Augusto", "Jose"],
    ["Marcos",],
    ["Joslen", "Miranda",(1,2,3,4,5)],
]

print(salas[2][2][2])

for sala,aluno in enumerate(salas):
    print(f"Sala {sala + 1}")
    for nome in aluno:
        print(f"\t{nome}")

