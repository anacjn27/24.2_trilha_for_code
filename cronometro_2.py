import os
import time

def inicializa_valores():
    segundo = 0
    minuto = 0
    hora = 0
    return segundo, minuto, hora

# a função define que para segundo = 60, o segundo vira zero e vai se adicionando 1 a minuto
def checa_seg_para_minuto(segundo, minuto, hora):
    if segundo == 60:
        segundo = 0
        if minuto == 59:
            minuto = 0
            hora += 1
        else:
            minuto += 1
    return segundo, minuto, hora

# para segundo/minuto/hora menor que 10, eles passam a ter um 0 na frente
def duas_casas_decimais(segundo, minuto, hora):
    if segundo < 10:
        segundo = f'0{segundo}'
    if minuto < 10:
        minuto = f'0{minuto}'
    if hora < 10:
        hora = f'0{hora}'
    return segundo, minuto, hora

def printa_hora(segundo, minuto, hora):
    print(f"{hora}:{minuto}:{segundo}")

def roda_relogio():
    segundo, minuto, hora = inicializa_valores()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        segundo, minuto, hora = checa_seg_para_minuto(segundo, minuto, hora)
        segundo_formatado, minuto_formatado, hora_formatada = duas_casas_decimais(segundo, minuto, hora)

        printa_hora(segundo_formatado, minuto_formatado, hora_formatada)

        time.sleep(1)
        segundo += 1

roda_relogio()
