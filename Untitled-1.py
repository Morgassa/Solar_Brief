import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

list_of_lists = [[4.73, 4.72, 4.58, 4.56, 4.68, 4.98, 5.05, 5.6, 5.22, 4.9, 4.81, 4.63], [4.54, 4.61, 4.58, 4.69, 4.95, 5.36, 5.41, 5.86, 5.28, 4.82, 4.63, 4.42], [4.45, 4.55, 4.56, 4.72, 5.03, 5.49, 5.52, 5.93, 5.28, 4.77, 4.55, 4.33], [4.69, 4.7, 4.58, 4.6, 4.75, 5.08, 5.15, 5.67, 5.25, 4.89, 4.77, 4.59]]
keys = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# plt.plot(x = keys[0], y = list_of_lists[0], marker='', color='olive', linewidth=2)
# plt.plot(x = keys[1], y = list_of_lists[1], marker='', color='red', linewidth=2)
# plt.plot(x = keys[2], y = list_of_lists[2], marker='', color='blue', linewidth=2)
# plt.plot(x = keys[3], y = list_of_lists[3], marker='', color='green', linewidth=2)

# t = np.linspace(1, 10, 1000)
fig = plt.figure(figsize=(15, 5))
fig.subplots_adjust(left=.06, right=.75, bottom=.1, top=.94)

# plt.title('subplot 1')
plt.ylabel('Radiação KWh.dia')
plt.suptitle('Radiação em xxxxnome aqui!', fontsize=16)

# plt.figure()
ax = fig.gca()


line1, = plt.plot(keys, list_of_lists[0], 'b-', label='Plano Horizontal')
line2, = plt.plot(keys, list_of_lists[1], 'r--', label='Ângulo igual a latitude')
line3, = plt.plot(keys, list_of_lists[2], 'y.-', label='Maior média anual')
line4, = plt.plot(keys, list_of_lists[3], 'g.-', label='Maior mínimo mensal')


# ax.set_xticks(np.arange(0, 10, 0.5))
ax.set_yticks(np.arange(4, 6.5, 0.1))
# ax.grid(True, 'major', 'y', ls='-.', lw=.5, c='gray', alpha=.3)
ax.grid(ls='-.', lw=.5, c='gray')
# plt.grid()

plt.legend()
plt.savefig('books_read.png')




# https://matplotlib.org/gallery/showcase/bachelors_degrees_by_gender.html#sphx-glr-gallery-showcase-bachelors-degrees-by-gender-py