#£ukasz Chmielowski gr 1 zad 4 lista 9


import matplotlib.pyplot as plt
import numpy as np

#dataset
val = [16.36, 16.26, 12.91, 12.21, 5.73, 4.64, 2.87, 2.5, 1.6, 1.39]
bars = ('Python', 'C', 'C++', 'Java', 'C#', 'Visual Basic', 'JavaScript', 'SQL', 'Assembly language', 'PHP')
y_pos = np.arange(len(val))

#rozmiar
plt.figure(figsize=(10,10))

#tworzymy slupki
plt.barh(y_pos, val, color = '#00ffff')

#podpisy
plt.yticks(y_pos, bars)

plt.ylabel('Jezyki', fontsize=12, color='#000000')
plt.xlabel('Popularnosc podana w %', fontsize=12, color='#000000')
plt.title('10 najpopularniejszych jezykow programowania', fontsize=16, color='#000000')

plt.show()