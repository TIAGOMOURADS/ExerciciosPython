l = float(input('Qual a largura da parede em metros? :'))
a = float(input('Qual a altura da parede em metros? :'))
total = l * a
t = total / 2
print('Para as medidas {} x {} corresponde a área {}m². \nSéra necessário {}L de tinta.'.format(l, a, total, t))
