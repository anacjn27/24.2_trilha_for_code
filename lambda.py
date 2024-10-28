def somar(x, y):
    return x + y
print(somar(x=10, y=5))

# a mesma coisa que a função de cima, todavia se forma mais reduzida

somar1 = lambda x, y: (x + y)
print(somar1(x=6, y=9))

aumento = lambda a, b: (a*b / 100)
print(aumento(a=100, b=6))