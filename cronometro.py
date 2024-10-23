# importando biblioteca que interage com o sistema operacional
import os

# importando biblioteca que introduz noção de tempo no Python.
import time

segundo = 0
minuto = 0

while True:
    os.system('cls')
    if segundo == 60:
        segundo = 0
        minuto = minuto + 1
    print(f'{minuto}:{segundo}')
    
    time.sleep(1)
    segundo = segundo + 1