from __future__ import absolute_import
from pyti import catch_errors
from pyti.exponential_moving_average import (
    exponential_moving_average as ema
    )


def moving_average_convergence_divergence(data, short_period, long_period):
    """
    Moving Average Convergence Divergence.

    Formula:
    EMA(DATA, P1) - EMA(DATA, P2)
    """
    catch_errors.check_for_period_error(data, short_period)
    catch_errors.check_for_period_error(data, long_period)

    macd = ema(data, short_period) - ema(data, long_period)
    return macd


def histogram(data, short_period, long_period, signal_length):
    """
     > MACD Line: (12-day EMA - 26-day EMA)

    Signal Line: 9-day EMA of MACD Line

    MACD Histogram: MACD Line - Signal Line
    """

    hist = moving_average_convergence_divergence(data, short_period, long_period) - ema(moving_average_convergence_divergence(data, short_period, long_period), signal_length)
    return hist



