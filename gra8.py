import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", "r") as settings:
    sett = [float(i) for i in settings.read().split("\n")]


dac_v = np.loadtxt("datavolts.txt", dtype=int)
tmes  = np.loadtxt("datatimes.txt", dtype=float)

volts = dac_v * sett[1]


fig, ax = plt.subplots(figsize=[10, 8], dpi=250)

ax.set_title("Зарядка и разрядка конденсатора от времени в RC цепи")

ax.set(xlabel='Время, с', ylabel='Напряжение, В')
ax.plot(tmes, volts, markevery=0.01, label='')
ax.plot(tmes, volts, 'o-b', markevery=0.04, label='Экспериментальные точки', markersize=4, color='b')
ax.text(20,0.5,"Время зарядки  = 15.81 сек")
ax.text(20,0.4,"Время разрядки = 20.49 сек")


ax.grid(which='major')
ax.minorticks_on()
ax.grid(which='minor', linestyle=':')

ax.legend()
fig.savefig("test.png")

plt.show()