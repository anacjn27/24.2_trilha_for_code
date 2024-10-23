import time
c = 0

# pass deixa o fluxo do while continuar
# break interrompe o fluxo do while
# continue interrompe apenas a interação atual

while True:
    if c == 11:
        break
    print(c)
    time.sleep(1)
    c = c + 1

print('O tempo acabou')