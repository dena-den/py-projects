from scipy import stats
from itertools import chain

df = [[15, 20], [17, 3]]

def check(df):
    if min(list(chain(*df))) < 5:
        fisher(df)
    else:
        pirson(df)

def fisher(df):
    print('fisher')
    odds_ratio, p_value = stats.fisher_exact(df)
    print(f'p-value = {p_value:.3f}')

def pirson(df):
    print('pirson')
    chi2_value, p_value, df_value, expected_array = stats.chi2_contingency(df, correction=True)
    print(f'Хи-квадрат = {chi2_value:.3f}, p-value = {p_value:.3f}, df = {df_value}')
    print(f'Ожидаемые значения:\n{expected_array}')

check(df)