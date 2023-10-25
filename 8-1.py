import numpy as np
import matplotlib.pyplot as plt

data_array = np.loadtxt("/home/b03-301/Documents/data.txt", dtype=int)
data_settings = np.loadtxt("/home/b03-301/Documents/settings.txt", dtype=float)
data_time = np.arange(0, (data_array.size / data_settings[0]), (1 / data_settings[0]))
data_array = data_array * data_settings[1]

k = round(data_array.size / data_settings[0] * 100) / 100

fig, ax = plt.subplots()

ax.minorticks_on()
ax.grid(which='minor',color='gray',linestyle=':')

ax.plot(data_time, data_array, color='navy', linestyle='-', linewidth=0.75, marker = 'o', markersize=3, markerfacecolor='white', markeredgewidth=1, markeredgecolor='red', markevery=12, label='V(t)')

ax.set_xlim(np.min(data_time), np.max(data_time))
ax.set_ylim(np.min(data_array), np.max(data_array))

ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

ax.set_title('Процесс заряда и разряда конденсатора в R-C цепи')

ax.legend()

ax.grid(True, color='gray', linestyle='-')

ax.legend()
plt.text(np.max(data_time) - 3.5, np.min(data_array) + 0.5, 'Время заряда: {} сек.'.format(k), fontsize=10, backgroundcolor='lemonchiffon')
plt.text(np.max(data_time) - 3.5, np.min(data_array) + 0.25, 'Конденсатор не разрядился :(', fontsize=10, backgroundcolor='lemonchiffon')

plt.show()
fig.savefig('/home/b03-301/Documents/graph.svg')