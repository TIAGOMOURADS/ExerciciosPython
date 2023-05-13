d = float(input('Quanto de dinheiro você tem na carteira? R$: '))
dolar = d / 4.94
euro = d / 5.43
print('Com R${:.2f} você pode comprar US${:.2f} Dolares ou €{:.2f} Euros'.format(d, dolar, euro))
