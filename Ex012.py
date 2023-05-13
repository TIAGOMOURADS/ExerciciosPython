p = float(input('Qual o preço do produto? R$: '))
d = p - (p * 0.05 / 100)
print('O valor anterior do produto era R${:.2f}, com o desconto de 5% ficou R${:.2f}'.format(p, d))
