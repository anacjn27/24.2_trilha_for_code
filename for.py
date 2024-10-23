# formas de se usar o for:
# com um generator. Ex.: for in range(10)
# com um iterador. Ex.: for n in [1, 2, 3, 4, 5]

# com iterador
lista = [2,7,0,4,5]

for teste in lista:
    if teste >= 4:
        print('verdadeiro')
    else:
        print('falso')

    print(teste)

# com generator

for i in range(11):
    print(i)