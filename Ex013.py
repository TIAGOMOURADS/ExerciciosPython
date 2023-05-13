sal = float(input('Qual é o salário do funcionário R$:'))
novo = sal + (sal * 0.15)
print('O salário do funcionário era R${:.2f}. com o aumento de 15% ficou R${:.2f}'.format(sal, novo))
