from sklearn.ensemble import RandomForestRegressor
import numpy as np

def test_regression_simple(data_scaled, data, features, label_col='Price', train_days=30, test_days=2):

    data['Price_next'] = data[label_col].shift(-1)
    data_scaled['Price_next'] = data['Price_next']
    data.dropna(inplace=True)
    data_scaled.dropna(inplace=True)

    total_correct = 0
    total_test_samples = 0

    n = len(data)
    step = train_days + test_days

    for start in range(0, n, step):
        train_start = start
        train_end = train_start + train_days

        test_start = train_end
        test_end = test_start + test_days

        if test_end > n or train_end > n:
            break

        X_train = data_scaled[features].iloc[train_start:train_end]
        y_train = data_scaled['Price_next'].iloc[train_start:train_end]

        X_test = data_scaled[features].iloc[test_start:test_end]
        y_test = data['Price_next'].iloc[test_start:test_end]

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)


        y_direction_true = (y_test.values - data[label_col].iloc[test_start:test_end].values > 0).astype(int)
        y_direction_pred = (y_pred - data[label_col].iloc[test_start:test_end].values > 0).astype(int)

        correct = (y_direction_true == y_direction_pred).sum()
        total_correct += correct
        total_test_samples += len(y_test)

    accuracy = total_correct / total_test_samples if total_test_samples > 0 else 0
    return accuracy
