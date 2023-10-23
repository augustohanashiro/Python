nome = "teste".__iter__()

print(nome)
print(iter(nome))
print(next(nome))
print(nome.__next__())
print(next(nome))
print(nome.__next__())