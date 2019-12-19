import numpy as np
import pandas as pd

spe_num, gen_num = list(map(int, input().split(' ')))

def flatter(x=[]):
    if x == []: return x
    else: return np.sum(x, axis=0)

spe = flatter([input().split(' ')[1:] for i in range(spe_num)])
gen = flatter([input().split(' ')[1:] for i in range(gen_num)])
date = sorted(set(spe + gen))

columns = ['special', 'general', 'sum']
df = pd.DataFrame(columns=columns, index=date)
for _date in date:
    df['special'][_date] = spe.count(_date)
    df['general'][_date] = gen.count(_date)
df['sum'] = df['special'] + df['general']

if spe_num != 0:
    ans = df['sum'][df['special'] == spe_num]
    ans_date, ans_num = ans.keys()[0], ans.values[0]
elif spe_num == 0:
    ans_num = df['sum'].max()
    ans_date = df.index[df['sum'] == df['sum'].max()][0]

print('{0} {1}\n'.format(ans_date, ans_num))task3
