import pandas as pd
import numpy as np

def label1(data):
    data_rev = data[::-1].reset_index(drop=True)

    n = len(data_rev)
    data_rev['label'] = pd.Series([np.nan]*n, dtype='object')

    for i in range(n - 1):
        if data_rev.loc[i + 1, 'Change %'] > 0:
            data_rev.loc[i, 'label'] = 'up'
        else:
            data_rev.loc[i, 'label'] = 'down'

    data_final = data_rev[::-1].reset_index(drop=True)

    return data_final

def label2(data):
    data_rev = data[::-1].reset_index(drop=True)

    n = len(data_rev)
    data_rev['label'] = pd.Series([np.nan]*n, dtype='object')

    for i in range(n - 1):
        if data_rev.loc[i + 1, 'Change %'] > 1:
            data_rev.loc[i, 'label'] = 'Buy'
        elif -1 < data_rev.loc[i + 1, 'Change %'] < 1:
            data_rev.loc[i, 'label'] = 'Hold'
        else:
            data_rev.loc[i, 'label'] = 'Sell'

    data_final = data_rev[::-1].reset_index(drop=True)

    return data_final
