from core.candle import candles
class AverageTrueRange:
    average_true_range_history = []

    '''
    OHLC
    '''

    def __init__(self, data, d):
        self.data = data
        self.d = d

    def average_true_range(self):
        while len(self.average_true_range_history) < len(self.data[3]):
            true_range = 0

            if len(self.average_true_range_history) <= 0:
                self.average_true_range_history.append(max(self.data[1][1] - self.data[2][1], abs(self.data[1][1] - self.data[3][0]),
                    abs(self.data[2][1] - self.data[3][0]))/1/self.d)



            if 1 < len(self.data[3]) < self.d:
                if self.data[1][-2] > self.data[2][-1]:
                    true_range = self.data[1][-2] - self.data[2][-1]
                elif self.data[2][-2] <= self.data[1][-1]:
                    true_range = self.data[1][-1] - self.data[2][-2]

                self.average_true_range_history.append(true_range)

            elif 1 < len(self.data[3]):
                true_range = 0

                if self.data[1][-2] > self.data[2][-1]:
                    true_range = self.data[1][-2] - self.data[2][-1]
                elif self.data[2][-2] <= self.data[1][-1]:
                    true_range = self.data[1][-1] - self.data[2][-2]

                average_tr = (((self.d - 1) * self.average_true_range_history[-1]) + true_range) / self.d
                self.average_true_range_history.append(average_tr)

        return self.average_true_range_history



atr = AverageTrueRange(data=candles(), d=14)


print(atr.average_true_range())


#
# '''
#
# OHLC
# '''
# from pandas import DataFrame
# def avg_true_range( df = candles()):
#   ind = range(0,len(df))
#   print(ind)
#   indexlist = list(ind)
#   df.index = indexlist
#
#   for index, row in df.iterrows():
#     if index != 0:
#       tr1 = row[1] - row[2]
#       tr2 = abs(row[1] - DataFrame[index-1][3])
#       tr3 = abs(row[2] - DataFrame[index-1][3])
#
#       true_range = max(tr1, tr2, tr3)
#       df.set_value(index,"True Range", true_range)
#
#   df["Avg TR"] = df["True Range"].rolling(min_periods=14, window=14, center=False).mean()
#   return df
#
#
# print(avg_true_range())
#



