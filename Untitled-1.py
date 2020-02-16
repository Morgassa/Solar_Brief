import pandas as pd
import matplotlib.pyplot as plt


dict1 = {'x1': [4.73, 4.72, 4.58, 4.56, 4.68, 4.98, 5.05, 5.6, 5.22, 4.9, 4.81, 4.63], 'x2': [4.54, 4.61, 4.58, 4.69, 4.95, 5.36, 5.41, 5.86, 5.28, 4.82, 4.63, 4.42], 'x3': [4.45, 4.55, 4.56, 4.72, 5.03, 5.49, 5.52, 5.93, 5.28, 4.77, 4.55, 4.33], 'x4': [4.69, 4.7, 4.58, 4.6, 4.75, 5.08, 5.15, 5.67, 5.25, 4.89, 4.77, 4.59]}

df = pd.DataFrame(dict1)


fig=plt.figure();

# df.plot.density()
plt.rc('lines', linewidth=4, color='g')
plt.savefig('books_read.png')
plt.show()