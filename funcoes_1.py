# o que são funções?

def soma(x, y):
    var_soma = x + y
    return var_soma

 #chamar a função soma
print(soma(x=10, y=5))

# new (se o número for igual a (qualquer número ), dividido por 2 ele vai dar resto 0? se sim, true é par)

def ehpar(numero):
    return numero % 2 == 0

print(ehpar(numero=10))

# função com parâmetro facultativo

def soma(x, y=10):
    var_soma = x - y
    return var_soma
print(soma(x=10))