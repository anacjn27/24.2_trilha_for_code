# utilizando o loop while
def fatorial(numero):
    fat = 1
    while numero > 1:
        fat *= numero
        numero -= 1
    return fat

print(fatorial(2))

# new

def fatorial1(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial1(numero - 1)
    
print(fatorial1(5))