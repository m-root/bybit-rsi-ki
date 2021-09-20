from pyti import exponential_moving_average as ema, smoothed_moving_average as sma, \
    hull_moving_average as hma, weighted_moving_average as wma
from core.candle import candles
from core.archirve.hashi_candle_close import heikin_ashi_close
import numpy as np

def trade_logic(pair, low_time_frame, higher_time_frame, fast_ma, slow_ma, restClient):
    candle_ltf = candles(pair, low_time_frame, restClient)
    candle_htf = candles(pair, higher_time_frame, restClient)
    ha_ltf = {'open': np.array(candle_ltf[0]), 'high': np.array(candle_ltf[1]),
              'low': np.array(candle_ltf[2]), 'close': np.array(candle_ltf[3])}
    ha_htf = {'open': np.array(candle_htf[0]), 'high': np.array(candle_htf[1]),
              'low': np.array(candle_htf[2]), 'close': np.array(candle_htf[3])}
    slow_maa = sma.smoothed_moving_average(candle_ltf[3], slow_ma)
    slowma = sma.smoothed_moving_average(heikin_ashi_close(ha_ltf), slow_ma)
    fastma = ema.exponential_moving_average(heikin_ashi_close(ha_htf), fast_ma)

    return [fastma, slowma, slow_maa]


def hull_trade_logic(pair, tFrame, firstSmooth, secondSmooth, restClient):
    # firstSmooth = 6
    # secondSmooth = 10

    print(000000000000000000)
    print(tFrame)
    print(pair)
    print(firstSmooth)
    print(secondSmooth)
    print(000000000000000000)


    hData = wma.weighted_moving_average(
        hma.hull_moving_average(
                candles(
                    symbol=pair,
                    interval = tFrame,
                    rest_client = restClient
                )[-1],
                firstSmooth

        ),
        secondSmooth
    )

    return hData



def quest(pair, tFrame, firstSmooth, rateSmooth, restClient):

    hData = hma.hull_moving_average(
                candles(
                    symbol=pair,
                    interval = tFrame,
                    rest_client = restClient
                )[-1],
                firstSmooth
        )

    # ls = []
    #
    # for i in range(0, len(hData) - 1):
    #     ls.append(((hData[i + 1] - hData[i]) / hData[i]) * 10000)
    #
    # return wma.weighted_moving_average(ls,rateSmooth)


    # for i in range(0, len(hData) - 1):
    #     ls.append(((hData[i + 1] - hData[i]) / hData[i]) * 10000)

    return wma.weighted_moving_average(hData,rateSmooth)

