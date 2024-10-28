#elevar ao quadrado cada item da lista
lista = [1,2,3,4]

def generator(lista):
    for i in lista:
        yield i**2

g = generator(lista)
for i in range(4):
    print(next(g))
