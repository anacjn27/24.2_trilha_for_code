 # calculadora de notas

nota1 = float(input('Digite sua nota da P1 >> '))
nota2 = float(input('Digite sua nota da P2 >> '))
nota_final = (nota1 + nota2)/2

if nota_final >= 7.0:
  print('Aprovado!')
elif nota_final >= 5.0:
  print('Recuperação')
else:
  print('Reprovado')
