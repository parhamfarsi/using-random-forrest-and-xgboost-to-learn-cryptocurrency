import pandas as pd
import numpy as np

def parabolic_sar(high, low, af_initial=0.02, af_step=0.02, af_max=0.2):


    n = len(high)
    sar = np.zeros(n)
    trend = 1
    af = af_initial
    ep = high[0]
    sar[0] = low[0]

    high = high[::-1]
    low = low[::-1]

    for i in range(1, n):
        sar[i] = sar[i-1] + af * (ep - sar[i-1])
        if trend == 1:
            if low[i] < sar[i]:
                trend = -1
                sar[i] = ep
                ep = low[i]
                af = af_initial
            else:
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + af_step, af_max)
                sar[i] = min(sar[i], low[i-1])
                if i > 1:
                    sar[i] = min(sar[i], low[i-2])
        else:
            if high[i] > sar[i]:
                trend = 1
                sar[i] = ep
                ep = high[i]
                af = af_initial
            else:
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + af_step, af_max)
                sar[i] = max(sar[i], high[i-1])
                if i > 1:
                    sar[i] = max(sar[i], high[i-2])
    sar = sar[::-1]
    return sar


def rsi(close, period=14):

    close = close[::-1]

    delta = np.diff(close)
    gains = np.where(delta > 0, delta, 0)
    losses = np.where(delta < 0, -delta, 0)

    n = len(close)
    rsi = np.zeros(n)
    rsi[:period] = np.nan

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    if avg_loss == 0:
        rsi[period] = 100 if avg_gain > 0 else 0
    else:
        rs = avg_gain / avg_loss
        rsi[period] = 100 - (100 / (1 + rs))

    for i in range(period + 1, n):
        current_gain = gains[i - 1]
        current_loss = losses[i - 1]
        avg_gain = ((avg_gain * (period - 1)) + current_gain) / period
        avg_loss = ((avg_loss * (period - 1)) + current_loss) / period
        if avg_loss == 0:
            rsi[i] = 100 if avg_gain > 0 else 0
        else:
            rs = avg_gain / avg_loss
            rsi[i] = 100 - (100 / (1 + rs))

    rsi = rsi[::-1]

    return rsi


def stochastic_oscillator(high, low, close, k_period=14, d_period=3):

    close = close[::-1]
    high = high[::-1]
    low = low[::-1]

    n = len(high)
    k = np.zeros(n)
    d = np.zeros(n)
    k[:k_period] = np.nan
    d[:k_period + d_period - 1] = np.nan

    for i in range(k_period - 1, n):
        lowest_low = np.min(low[i - k_period + 1:i + 1])
        highest_high = np.max(high[i - k_period + 1:i + 1])
        if highest_high == lowest_low:
            k[i] = 0
        else:
            k[i] = 100 * (close[i] - lowest_low) / (highest_high - lowest_low)

    for i in range(k_period + d_period - 2, n):
        d[i] = np.mean(k[i - d_period + 1:i + 1])
    
    k = k[::-1]
    d = d[::-1]

    return k, d


def obv(close, volume):
    close = close[::-1]
    volume = volume[::-1]
    n = len(close)
    obv = np.zeros(n)
    obv[0] = 0

    for i in range(1, n):
        if close[i] > close[i-1]:
            obv[i] = obv[i-1] + volume[i]
        elif close[i] < close[i-1]:
            obv[i] = obv[i-1] - volume[i]
        else:
            obv[i] = obv[i-1]

    obv = obv[::-1]

    return obv


def mfi(high, low, close, volume, period=14):

    close = close[::-1]
    high = high[::-1]
    low = low[::-1]
    volume = volume[::-1]

    high = pd.Series(high)
    low = pd.Series(low)
    close = pd.Series(close)

    n = len(high)
    mfi = np.zeros(n)
    mfi[:period] = np.nan
    

    typical_price = (high + low + close) / 3
    raw_money_flow = typical_price * volume

    positive_flow = np.zeros(n)
    negative_flow = np.zeros(n)

    for i in range(1, n):
        if typical_price[i] > typical_price[i-1]:
            positive_flow[i] = raw_money_flow[i]
        elif typical_price[i] < typical_price[i-1]:
            negative_flow[i] = raw_money_flow[i]

    for i in range(period, n):
        positive_sum = np.sum(positive_flow[i - period + 1:i + 1])
        negative_sum = np.sum(negative_flow[i - period + 1:i + 1])
        if negative_sum == 0:
            mfi[i] = 100 if positive_sum > 0 else 0
        else:
            money_flow_ratio = positive_sum / negative_sum
            mfi[i] = 100 - (100 / (1 + money_flow_ratio))

    mfi = mfi[::-1]    

    return mfi


def bollinger_bands(close, period=20, k=2):

    close = close[::-1]

    n = len(close)
    middle_band = np.zeros(n)
    upper_band = np.zeros(n)
    lower_band = np.zeros(n)
    middle_band[:period-1] = np.nan
    upper_band[:period-1] = np.nan
    lower_band[:period-1] = np.nan

    for i in range(period-1, n):
        middle_band[i] = np.mean(close[i-period+1:i+1])
        std_dev = np.std(close[i-period+1:i+1], ddof=0)
        upper_band[i] = middle_band[i] + k * std_dev
        lower_band[i] = middle_band[i] - k * std_dev

    middle_band = middle_band[::-1]
    upper_band = upper_band[::-1]
    lower_band = lower_band[::-1]

    return middle_band, upper_band, lower_band


def atr(high, low, close, period=14):

    high = high[::-1]
    close = close[::-1]
    low = low[::-1]

    n = len(high)
    tr = np.zeros(n)
    atr = np.zeros(n)
    tr[0] = high[0] - low[0]
    atr[:period] = np.nan

    for i in range(1, n):
        tr[i] = max(
            high[i] - low[i],
            abs(high[i] - close[i-1]),
            abs(close[i-1] - low[i])
        )

    atr[period] = np.mean(tr[1:period+1])

    for i in range(period + 1, n):
        atr[i] = ((atr[i-1] * (period - 1)) + tr[i]) / period

    atr = atr[::-1]

    return atr


def sma(close, period=20):

    close = close[::-1]

    n = len(close)
    sma_values = np.zeros(n)
    sma_values[:period-1] = np.nan

    for i in range(period-1, n):
        sma_values[i] = np.mean(close[i-period+1:i+1])

    sma_values = sma_values[::-1]

    return sma_values


def ema(close, period=20):

    close = close[::-1]

    n = len(close)
    ema_values = np.zeros(n)
    ema_values[:period-1] = np.nan


    ema_values[period-1] = np.mean(close[:period])


    alpha = 2 / (period + 1)


    for i in range(period, n):
        ema_values[i] = alpha * close[i] + (1 - alpha) * ema_values[i-1]

    ema_values = ema_values[::-1]


    return ema_values