from datetime import datetime, timedelta, timezone

def candles( symbol, interval, rest_client):

    klines = [list(d.values()) for d in rest_client.get_kline( symbol=symbol, interval=interval)['result']]
    cand = []

    for kline in klines:
        f = [
            (datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=kline[2] / 1000)),
            kline[3],
            kline[4],
            kline[5],
            kline[6],
            kline[7]
        ]
        cand.append(f)

    return[
        [float(d[1]) for d in cand],
        [float(d[2]) for d in cand],
        [float(d[3]) for d in cand],
        [float(d[4]) for d in cand]
        ]


