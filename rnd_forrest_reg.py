import pandas as pd
#from pandasgui import show
import numpy as np
from sklearn.preprocessing import StandardScaler
import functions as f
import read_csv as read
import date 
import clean_data as clean
import label 
import test_reg as test
import indicators as indc


file_path = 'XRP Historical Data.csv'

all_data = read.read_csv(file_path)
data = clean.cleanData(all_data)
all_data = label.label1(all_data)
all_data = indc.indicators(all_data)

#show(all_data)

data = all_data
#show(data)
data.dropna(inplace=True)

features_to_log = ['Price', 'Open', 'High', 'Low', 'Upper_band', 'Lower_band']
for feature in features_to_log:
    data[feature] = np.log(data[feature])
features = ['Price','Open','High','Low','Vol.','RSI', 'Middle_band', 'Upper_band','ATR', 'Lower_band', 'OBV',  'SMA', 'EMA']
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[features])
data_scaled = pd.DataFrame(data_scaled, columns=features)


accuracy = test.test_regression_simple(data,data,features)
print(accuracy)