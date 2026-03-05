import numpy as np
import matplotlib.pyplot as plt

xarray = np.array(range (1,11))
y1array = np.array([101,103,107,109,113,127,131,137,139,149])
y2array= np.array(sorted(list(range(121,131)), reverse=True))

plt.figure(figsize=(10,6))
plt.plot(xarray, y1array, label =  'Series 1')
plt.plot(xarray, y2array, label =  'Series 2')

plt.title('Graph of teo number series')
plt.legend

plt.grid(False)
plt.show()