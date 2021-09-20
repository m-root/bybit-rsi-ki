from pyti.average_true_range import average_true_range as atr
from core.candle import candles
from numpy import mean

candles_coll = candles(symbol="TRXUSDT", interval="15m")
print(mean(atr(candles_coll[-1], 14)[-100:-2]))
print(mean(atr(candles_coll[-1], 14)[-50:-2]))
print(atr(candles_coll[-1], 21)[-22:])
print()
print()
print()
print()
print(mean(atr(candles_coll[-1], 14)[-(20+2):-2])) #TODO use this one
print(mean(atr(candles_coll[-1], 14)[-2])) #TODO use this one
print((atr(candles_coll[-1], 14)[-23:-2]))
print()
print()
print()
print((atr(candles_coll[-1], 14)[-15:-2]))
print(min(atr(candles_coll[-1], 14)[-15:-2]))
print(atr(candles_coll[-1], 21))
# print(len(atr(candles_coll[-1], 14)[-23:-2]))

