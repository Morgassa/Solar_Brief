import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

list_of_lists = [[4.73, 4.72, 4.58, 4.56, 4.68, 4.98, 5.05, 5.6, 5.22, 4.9, 4.81, 4.63], [4.54, 4.61, 4.58, 4.69, 4.95, 5.36, 5.41, 5.86, 5.28, 4.82, 4.63, 4.42], [4.45, 4.55, 4.56, 4.72, 5.03, 5.49, 5.52, 5.93, 5.28, 4.77, 4.55, 4.33], [4.69, 4.7, 4.58, 4.6, 4.75, 5.08, 5.15, 5.67, 5.25, 4.89, 4.77, 4.59]]

keys = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

data = pd.DataFrame()


meses = data['mes'] = keys
plan_horizon = data['Plano Horizontal'] = list_of_lists[0]
equal_latitude = data['Ângulo igual a latitude'] = list_of_lists[1]
maior_media = data['Maior média anual'] = list_of_lists[2]
maior_minimo = data['Maior mínimo mensal'] = list_of_lists[3]

media =data['Plano Horizontal'].median()


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.axhline(media, color='gray', linestyle='dotted', label='Radiação Média')
ax1.plot(meses, plan_horizon, color='r', linestyle='--', label='Plano Horizontal')
ax2.plot(meses, equal_latitude, color='b', linestyle='-.', label='Ângulo igual a latitude')
ax2.plot(meses, maior_media, color='g', linestyle='-', label='Maior média anual')
ax2.plot(meses, maior_minimo, color='y', linestyle='-', label='Maior mínimo mensal')



ax1.legend()
ax1.set_title('Median Salary (LOLS) by Age')
# ax1.set_xlabel('Mês')
ax1.set_ylabel('Radiação por M²')


ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Mês')
ax2.set_ylabel('Radiação por M²')

plt.tight_layout()

plt.savefig('books_read1.png')

# print(data)

# fig = plt.figure(figsize=(15, 5))
# fig.subplots_adjust(left=.06, right=.75, bottom=.1, top=.94)

# plt.title('subplot 1')
# plt.ylabel('Radiação KWh.dia')
# # plt.suptitle('Radiação em xxxxnome aqui!', fontsize=16)

# ax = fig.gca()


# line1, = plt.plot(keys, list_of_lists[0], 'b:^', label='Plano Horizontal')
# line2, = plt.plot(keys, list_of_lists[1], 'r-.D', label='Ângulo igual a latitude')
# line3, = plt.plot(keys, list_of_lists[2], 'y--s', label='Maior média anual')
# line4, = plt.plot(keys, list_of_lists[3], 'g--o', label='Maior mínimo mensal')


# # ax.set_xticks(np.arange(0, 10, 0.5))
# ax.set_yticks(np.arange(4, 6.5, 0.1))
# # ax.grid(True, 'major', 'y', ls='-.', lw=.5, c='gray', alpha=.3)
# ax.grid(ls='-.', lw=.5, c='gray')
# # plt.grid()
# fig.tight_layout(pad=1)
# plt.legend(loc='best', prop={'size':'large'})
# plt.savefig('books_read1.png')




# https://matplotlib.org/gallery/showcase/bachelors_degrees_by_gender.html#sphx-glr-gallery-showcase-bachelors-degrees-by-gender-py