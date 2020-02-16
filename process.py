# Localidades próximas

mês = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

olinda = [2.9, 5.89, 6.01, 5.93, 5.25, 4.54, 4.25, 4.40, 5.17, 5.66, 6.04, 6.20, 6.20]	
recife = [8.4, 5.73, 5.88, 5.81, 5.15, 4.44, 4.14, 4.26, 4.98, 5.38, 5.72, 5.96, 5.98]



#//*[@id="tb_sundata"]/tbody

#//*[@id="data_output"]/table[2]/tbody


for row in range(1,4):
    for element in range(1,23):
        print ('//*[@id="tb_sundata"]/tbody/tr[{}]/td[{}]'.format(row, element))



