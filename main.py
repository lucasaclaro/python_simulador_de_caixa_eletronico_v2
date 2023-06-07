valor = int(input('Digite o valor do saque: '))
saldo = valor

nota_100 = saldo // 100
saldo = saldo % 100

nota_50 = saldo // 50
saldo = saldo % 50

nota_20 = saldo // 20
saldo = saldo % 20

nota_10 = saldo // 10
saldo = saldo % 10

nota_5 = saldo // 5
saldo = saldo % 5

nota_2 = saldo // 2
saldo = saldo % 2

nota_1 = saldo // 1

print('***' * 15)
print(f'Processando o pagamento...')
print('***' * 15)

print(f'Você receberá:\n'
      f'{nota_100} nota(s) de R$ 100,\n'
      f'{nota_50} nota(s) de R$ 50,\n'
      f'{nota_20} nota(s) de R$ 20,\n'
      f'{nota_10} nota(s) de R$ 10,\n'
      f'{nota_5} nota(s) de R$ 5,\n'
      f'{nota_2} nota(s) de R$ 2,\n'
      f'{nota_1} nota(s) de R$ 1.')

print('***' * 15)
print('\n...Programa encerrado.')
