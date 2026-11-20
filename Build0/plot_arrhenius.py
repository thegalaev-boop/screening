from cleaning import load_clean_data, to_arrhenius_point
from matplotlib import pyplot as plt
data = load_clean_data('raw_conductivity.csv')
x = []
y = []
for point in data:
    pair = list(to_arrhenius_point(point['temp_c'], point['sigma']))
    x.append(pair[0])
    y.append(pair[1])
plt.xlabel('1000/T (K^-1)')
plt.ylabel('log10(sigma) [S/cm]')
plt.title('Conductivity vs. Inverse temperature')
plt.scatter(x, y, c = 'blue', s = 10)
plt.grid(True)
plt.savefig('attempt1.png')
plt.show()
