import functions as f

def indicators(all_data):
    all_data['RSI'] = f.rsi(all_data['Price'])
    [all_data['Middle_band'],all_data['Upper_band'],all_data['Lower_band']] = f.bollinger_bands(all_data['Price'])
    all_data['ATR'] = f.atr(all_data['High'],all_data['Low'],all_data['Price'])
    all_data['OBV'] = f.obv(all_data['Price'],all_data['Vol.'])
    all_data['EMA'] = f.ema(all_data['Price'])
    all_data['SMA'] = f.sma(all_data['Price'])
    all_data['MFI'] = f.mfi(all_data['High'],all_data['Low'], all_data['Price'], all_data['Vol.'])
    all_data['k'],all_data['d'] = f.stochastic_oscillator(all_data['High'], all_data['Low'], all_data['Price'])
    all_data['SAR'] = f.parabolic_sar(all_data['High'],all_data['Low'])

    return all_data