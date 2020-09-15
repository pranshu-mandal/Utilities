#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Constants
c=299792458
ε = 1.8e-4
η_0 = 0.6

x_18 = np.array([ 86, 86, 86, 86, 110, 110, 115, 115])
x_19 = np.array([23, 23, 23, 23, 23, 23, 43, 43, 43, 43, 43, 110, 110])
y_18 = np.array([ 34, 35, 40, 41, 35, 35, 30, 29])
y_19 = np.array([64, 64, 61, 61, 56.8, 60.5, 57.8, 52, 55, 60, 57, 30.7, 31])
y_err_18 = np.array([2, 2, 2, 2, 2, 2, 2, 2])
y_err_19 = np.array([1, 1, 1, 1, 3.6, 3.8, 3.9, 3, 2, 2, 2, 2.6, 2.6])

our_result_x = np.array([100])
our_result_y = np.array([23.69])
our_result_y_err = np.array([8])

# Ruze equation
def convert(arr):
	return(c / (arr*1e9))

def ruze(arr):
	return (η_0 * np.exp(-((4*np.pi*ε)/arr)**2))
# dummy_x = np.arange(3,13,0.1)
# print(dummy_x)


# plt.scatter(x_18, y_18,  color='teal')
plt.errorbar(1000*convert(x_18), y_18, y_err_18, capsize=3, fmt='.k', label='Reported 2018')
plt.errorbar(1000*convert(x_19), y_19, y_err_19, capsize=3, fmt='.r', label='Reported 2019')

plt.errorbar(1000*convert(our_result_x), our_result_y, our_result_y_err, capsize=3,
 fmt='o', ecolor='g', capthick=2, label='$\eta_{\mathrm{A}}(\%)$ (2019)')

plt.plot(1000*convert(x_18), 100*ruze(convert(x_18)), '--', color='k', linewidth=1, label="Ruze equation fit 2018")
plt.plot(1000*convert(x_19), 100*ruze(convert(x_19)), '--', color='r', linewidth=1, label="Ruze equation fit 2019")

# f = interp1d(1000*convert(x_19), 100*ruze(convert(x_19)), kind='cubic')
# plt.plot(dummy_x, f(dummy_x))

plt.title('$\eta_{\mathrm{A}}(\%)$ from NRO 45m observations in 2018-2019')
plt.xlabel('Wavelength (mm)')
plt.ylabel('$\eta_{\mathrm{A}}(\%)$')
plt.legend()
# plt.savefig('eta_A_Mars.png')
plt.show()
