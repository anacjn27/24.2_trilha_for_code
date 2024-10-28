a = 0

# global a, torna a=10 a variável global
def escopo1():
    global a
    a = 10

escopo1()

print(a)