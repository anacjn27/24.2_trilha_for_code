# usando o loop for para inteirar a lista
numeros_pares_ate_20 = []

for i in range(11):
    numeros_pares_ate_20.append(i*2)

print(numeros_pares_ate_20)

#usando o loop for dentro da própria lista

pares_ate_40 = [i*2 for i in range(21)]
print(pares_ate_40)