import scipy.stats
observed_array = [38, 62]
expected = sum(observed_array) / len(observed_array)
chi2 = 0
for i in range(len(observed_array)):
    chi2 += ((observed_array[i] - expected)**2) / expected
print('Хи-квадрат Пирсона равен: ', chi2)
#find p-value
p_value = scipy.stats.t.sf(abs(chi2), df=1)
print('p-value равен: ', p_value)