import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Rascunho import solar_gather_bot

bot = solar_gather_bot()

bot.driver.get("http://www.cresesb.cepel.br/index.php?section=sundata&")

Latitude = '8.0113981'
Longitude = '38.8734516'

bot.put_coords()

resp = bot.get_angle_data()

print(resp)
print('-x-')


for i in resp:
    print(i)
    print('')


    print(i[0][0])
    print(i[0][1])
    print(i[0][2])
    print(i[0][3])

    png_name = '{}_x_{}.png'.format(i[0][2], i[0][3])

    # print(i[3][2:14])


    list_of_lists = [i[0][2:14], i[1][2:14], i[2][2:14], i[3][2:14]]


    # list_of_lists = [[4.73, 4.72, 4.58, 4.56, 4.68, 4.98, 5.05, 5.6, 5.22, 4.9, 4.81, 4.63], [4.54, 4.61, 4.58, 4.69, 4.95, 5.36, 5.41, 5.86, 5.28, 4.82, 4.63, 4.42], [4.45, 4.55, 4.56, 4.72, 5.03, 5.49, 5.52, 5.93, 5.28, 4.77, 4.55, 4.33], [4.69, 4.7, 4.58, 4.6, 4.75, 5.08, 5.15, 5.67, 5.25, 4.89, 4.77, 4.59]]



    plt.style.use('seaborn')


    keys = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    data = pd.DataFrame()


    meses = data['mes'] = keys
    plan_horizon = data['Plano Horizontal'] = list_of_lists[0]
    equal_latitude = data['Ângulo igual a latitude'] = list_of_lists[1]
    maior_media = data['Maior média anual'] = list_of_lists[2]
    maior_minimo = data['Maior mínimo mensal'] = list_of_lists[3]

    # media ='{:.2f}'.format(data['Plano Horizontal'].median())
    
    media = data['Plano Horizontal'].median()



    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

    ax1.axhline(media, color='gray', linestyle='dotted', label='Radiação Média')
    ax1.plot(meses, plan_horizon, color='r', linestyle='--', label='Plano Horizontal')

    ax1.text('Jan', media +.01, '{:.2f}'.format(media), color='black')

    ax2.plot(meses, equal_latitude, color='b', linestyle='-.', label='Ângulo igual a latitude')
    ax2.plot(meses, maior_media, color='g', linestyle='-', label='Maior média anual')
    ax2.plot(meses, maior_minimo, color='y', linestyle='-', label='Maior mínimo mensal')



    ax1.legend()
    ax1.set_title('Irradiação solar diária média mensal [kWh/m2.dia]')
    ax1.set_ylabel('Irradiação (kWh/m2.dia)')


    ax2.legend()
    ax2.set_xlabel(media)
    ax2.set_ylabel('Irradiação (kWh/m2.dia)')

    plt.tight_layout()

    # plt.savefig('books_read1.png')

    plt.savefig(png_name)



















# print(i[0][0])
# print(i[0][1])
# print(i[0][2])
# print(i[0][3])

# png_name = '{}_x_{}.png'.format(i[0][0][0], i[0][0][1])

# print(i[0][3][2:14])


# list_of_lists = [i[0][0][2:14], i[0][1][2:14], i[0][2][2:14], i[0][3][2:14]]


# # list_of_lists = [[4.73, 4.72, 4.58, 4.56, 4.68, 4.98, 5.05, 5.6, 5.22, 4.9, 4.81, 4.63], [4.54, 4.61, 4.58, 4.69, 4.95, 5.36, 5.41, 5.86, 5.28, 4.82, 4.63, 4.42], [4.45, 4.55, 4.56, 4.72, 5.03, 5.49, 5.52, 5.93, 5.28, 4.77, 4.55, 4.33], [4.69, 4.7, 4.58, 4.6, 4.75, 5.08, 5.15, 5.67, 5.25, 4.89, 4.77, 4.59]]



# plt.style.use('seaborn')


# keys = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# data = pd.DataFrame()


# meses = data['mes'] = keys
# plan_horizon = data['Plano Horizontal'] = list_of_lists[0]
# equal_latitude = data['Ângulo igual a latitude'] = list_of_lists[1]
# maior_media = data['Maior média anual'] = list_of_lists[2]
# maior_minimo = data['Maior mínimo mensal'] = list_of_lists[3]

# media =data['Plano Horizontal'].median()


# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

# ax1.axhline(media, color='gray', linestyle='dotted', label='Radiação Média')
# ax1.plot(meses, plan_horizon, color='r', linestyle='--', label='Plano Horizontal')
# ax2.plot(meses, equal_latitude, color='b', linestyle='-.', label='Ângulo igual a latitude')
# ax2.plot(meses, maior_media, color='g', linestyle='-', label='Maior média anual')
# ax2.plot(meses, maior_minimo, color='y', linestyle='-', label='Maior mínimo mensal')



# ax1.legend()
# ax1.set_title('Median Salary (LOLS) by Age')
# ax1.set_ylabel('Radiação por M²')


# ax2.legend()
# ax2.set_xlabel('Mês')
# ax2.set_ylabel('Radiação por M²')

# plt.tight_layout()

# # plt.savefig('books_read1.png')

# plt.savefig(png_name)
