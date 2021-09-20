import time
from m_run.novatron.m_core import logic
from datetime import datetime
from m_run.novatron import settings
import ast


def main():
    while True:
        pairs = open('pairs_main.txt', 'r')
        pairs = pairs.read()
        print(pairs)
        pairs = ast.literal_eval(pairs)
        if len(pairs) == 0:
            print('There are no pairs added')


        else:
            for pair in pairs:
                try:
                    print(pair)
                    logic(pair, settings.period)
                    time.sleep(1)

                except Exception as e:
                    print(e)
                    time.sleep(15)

        while float(datetime.utcnow().strftime("%M.%S")) % 15 != 0:
            time.sleep(1)


if __name__ == '__main__':
    main()

'Percentage Increment'
