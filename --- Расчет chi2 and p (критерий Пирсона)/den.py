from scipy import stats
import itertools
observed_array = [ [20, 15], [11, 12], [7, 9] ]
chi2_value, p_value, df_value, expected_array = stats.chi2_contingency(observed_array, correction=True)
# 'correction=True' - поправка Йейтса (только при df=1)
print(f'Хи-квадрат = {chi2_value:.3f}, p-value = {p_value:.3f}, df = {df_value}')
print(f'Ожидаемые значения:\n{expected_array}')
arr = observed_array - expected_array
num = max(list(itertools.chain(*arr)))
print(f'Максимальное значение стандартного отклонения {num}')