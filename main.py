falta_pao = True
falta_mel = False

if falta_mel and falta_pao:
    print('AND: Precisamos ir ao mercado')

if falta_mel or falta_pao:
    print('OR: Precisamos ir ao mercado')