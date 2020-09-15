#!/usr/bin/python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
# y = np.array([5, 20, 14, 32, 22, 38])

x = np.array([23, 23, 23, 23, 43, 43, 43, 43, 75, 75, 86, 86, 86, 86, 110, 110, 115, 115]).reshape((-1, 1))
y = np.array([73, 72, 74, 73, 73, 74, 72, 68, 54, 56, 42, 44, 49, 50, 42, 39, 36, 35])
y_err = np.array([2, 2, 2, 2, 4, 5, 3, 3, 3, 3, 4, 4, 3, 4, 2, 2, 3, 3])

our_result_x = np.array([100])
our_result_y = np.array([34.43])
our_result_y_err = np.array([12])


model = LinearRegression()

model.fit(x, y)

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

plt.scatter(x, y,  color='teal')
plt.errorbar(x, y, y_err, capsize=3, fmt='.k', label='Reported')

plt.errorbar(our_result_x, our_result_y, our_result_y_err, capsize=3,
 fmt='o', ecolor='g', capthick=2, label='Mars observation')

plt.plot(x, y_pred, color='red', linewidth=2)

plt.title('$\eta_{\mathrm{mb}}(\%)$ from NRO 45m observations in 2018-2019')
plt.xlabel('Frequency (GHz)')
plt.ylabel('$\eta_{\mathrm{mb}}(\%)$')
plt.legend()
# plt.savefig('eta_mb_Mars.png')
plt.show()

y_pred = model.predict(np.array([100]).reshape((-1, 1)))
print('predicted response:', y_pred, sep='\n')


x = np.array([23, 23, 23, 23, 43, 43, 43, 43, 75, 75, 86, 86, 86, 86, 110, 110, 115, 115]).reshape((-1, 1))
y = np.array([64, 64, 61, 61, 52, 55, 60, 57, 49, 52, 34, 35, 40, 41, 35, 35, 30, 29])
y_err = np.array([1, 1, 1, 1, 3, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2])

our_result_x = np.array([100])
our_result_y = np.array([23.69])
our_result_y_err = np.array([8])


model = LinearRegression()

model.fit(x, y)

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

plt.scatter(x, y,  color='teal')
plt.errorbar(x, y, y_err, capsize=3, fmt='.k', label='Reported')

plt.errorbar(our_result_x, our_result_y, our_result_y_err, capsize=3,
 fmt='o', ecolor='g', capthick=2, label='Mars observation')

plt.plot(x, y_pred, color='red', linewidth=2)

plt.title('$\eta_{\mathrm{A}}(\%)$ from NRO 45m observations in 2018-2019')
plt.xlabel('Frequency (GHz)')
plt.ylabel('$\eta_{\mathrm{A}}(\%)$')
plt.legend()
# plt.savefig('eta_A_Mars.png')
plt.show()

y_pred = model.predict(np.array([100]).reshape((-1, 1)))
print('predicted response:', y_pred, sep='\n')