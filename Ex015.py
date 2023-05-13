d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos km foi percorridos? '))
total = (d * 60) + (k * 0.15)
print('O valor total a ser pago é igual a R${:.2f}'.format(total))
