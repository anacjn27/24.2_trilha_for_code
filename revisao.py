variavel = 0
##
def fatorial(numero):
    global variavel
    variavel = 5
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero + fatorial(numero - 1)
print(fatorial(numero=3))

##
nome_da_funcao = lambda n: n*n**2

print(nome_da_funcao(n=3))

##
lista = [x**2 for x in range(10)]
print(lista)

##
try:
    int("jidfjgrijr")
except:
    print("Não foi possível converter")

##
def gen(n):
    lista = [i for i in range(n)]
    for i in lista:
        yield i
    
var1 = gen(10)
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
