# from m_run.crypto_signals.settings import rest_client
from datetime import datetime, timedelta, timezone

'''
OHLC
[1571038200000, T
'8304.98000000', O
'8305.00000000', H
'8298.14000000', L
'8300.44000000', C
'206.74020300', V
1571039099999, 
'1716154.84781088',
 1137, 
 '156.63597300', 
 '1300202.17170330', 
 '0']
 
 
 
 
 
'''


def candles(symbol, interval, rest_client):

    klines = rest_client.get_klines(symbol=symbol, interval=interval, startTime = '1514764800' , endtTime =  '1514774800',)
    # cand = []
    #
    # for kline in klines:
    #     f = [
    #         (datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=kline[0] / 1000)),
    #         kline[1],
    #         kline[2],
    #         kline[3],
    #         kline[4],
    #         kline[5]
    #     ]
    #     cand.append(f)
    #
    # return[
    #     [float(d[2]) for d in cand],
    #     [float(d[3]) for d in cand],
    #     [float(d[4]) for d in cand],
    #     [float(d[5]) for d in cand]
    #     ]
    return klines


def candles_wv(symbol, interval, rest_client):
    # print(symbol)
    klines = rest_client.klines(symbol=symbol, interval=interval)
    cand = []

    for kline in klines:
        f = [
            (datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=kline.open_time / 1000)),
            (datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=kline.close_time/ 1000)),
            kline.open,
            kline.high,
            kline.low,
            kline.close,
            kline.volume
            # OHLC
        ]
        cand.append(f)

    return[
        [float(d[2]) for d in cand],
        [float(d[3]) for d in cand],
        [float(d[4]) for d in cand],
        [float(d[5]) for d in cand]
        # [float(d[6]) for d in cand]
        ]
#
# # for d in candles('BTCUSDT', '15m', rest_client):
# #     print(d)
# from m_run.liquidex.settings import rest_client
#
# print(candles('BTCUSDT','15m',rest_client))