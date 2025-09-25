import pandas as pd
import numpy as np

def cleanData(data):
    for i in data:
        if i != 'Date':
            cleaned = []
            for x in data[i]:
                str_x = str(x).replace('%','').replace('/','').replace(',','').replace('$','') \
                              .replace('K','e3').replace('M','e6').replace('B','e9').strip()
                if str_x == '':
                    cleaned.append(None)  # or you could use 0.0 or skip
                else:
                    cleaned.append(float(str_x))
            data[i] = cleaned
    return data

