import numpy as np

def heikin_ashi_close(df):
    HA_Close = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    HACLOSE = np.array(HA_Close)
    return HACLOSE

