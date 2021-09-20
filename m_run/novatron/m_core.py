import pytz
from celery import Celery
from kombu import Exchange, Queue
from payload.payload import Payload
from datetime import datetime
from m_run.novatron import settings
from engine.trading_logic import TradingLogic
from celery import bootsteps

buy_list = []
sell_list = []

buy_list_list = []
sell_list_list = []

default_queue_name = 'default'
default_exchange_name = 'default'
default_routing_key = 'default'
deadletter_suffix = 'deadletter'
deadletter_queue_name = default_queue_name + f'.{deadletter_suffix}'
deadletter_exchange_name = default_exchange_name + f'.{deadletter_suffix}'
deadletter_routing_key = default_routing_key + f'.{deadletter_suffix}'


class DeclareDLXnDLQ(bootsteps.StartStopStep):
    """
    Celery Bootstep to declare the DL exchange and queues before the worker starts
        processing tasks
    """
    requires = {'celery.worker.components:Pool'}

    def start(self, worker):
        app = worker.app

        # Declare DLX and DLQ
        dlx = Exchange(deadletter_exchange_name, type='direct')

        dead_letter_queue = Queue(
            deadletter_queue_name, dlx, routing_key=deadletter_routing_key)

        # with worker.app.pool.acquire() as conn:
        #     dead_letter_queue.bind(conn).declare()


app = Celery(
    'tasks',
    broker='amqp://guest@localhost:5672//',
    backend='amqp://'
)

default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key,
    queue_arguments={
        'x-dead-letter-exchange': deadletter_exchange_name,
        'x-dead-letter-routing-key': deadletter_routing_key
    })

app.conf.task_queues = (default_queue,)

# Add steps to workers that declare DLX and DLQ if they don't exist
app.steps['worker'].add(DeclareDLXnDLQ)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key

currentTime = datetime.utcnow().strftime("%M")


@app.task(name='buy')
def buy(pair, traded_pairs):
    '''pair, low_time_frame, higher_time_frame, fast_ma, slow_ma, rest_client'''
    payload = Payload(base_asset=pair[0], cross_asset=pair[1], chat_id=settings.chat_id, settings=settings,
                      time_frame=settings.period)
    print('****************************************')
    print('****************************************')
    print('********** MARKER 2 *****************')
    print('****************************************')
    print('****************************************')
    return payload.buy_logic()


@app.task(name='sell')
def sell(pair):
    payload = Payload(base_asset=pair[0], cross_asset=pair[1], chat_id=settings.chat_id, settings=settings,
                      time_frame=settings.period)
    return payload.sell_logic()


def logic(pair, time_frame):
    print()
    print()
    print('****************************************')
    print('\t\t\t', pair[0] + pair[1])
    print('****************************************')
    Logic = TradingLogic(pair=pair[0] + pair[1], settings=settings)
    print('Buy is {}'.format(Logic.buyLogic() and pair[0] + pair[1] not in buy_list))
    print()
    print('Sell is {}'.format(Logic.sellLogic() and pair not in sell_list))
    print('****************************************')
    print(str(datetime.now(pytz.timezone('Africa/Nairobi'))))
    print('****************************************')
    if Logic.buyLogic() \
            and pair[0] + pair[1] not in buy_list:
        print(buy.delay(pair, len(buy_list_list)))
        print(str(datetime.now(pytz.timezone('Africa/Nairobi'))))
        print('****************************************')
        print('****************************************')
        if pair[0] + pair[1] not in buy_list:
            buy_list.append(pair[0] + pair[1])
            buy_list_list.append(pair)
            if pair[0] + pair[1] in sell_list or pair in sell_list_list:
                sell_list.remove(pair[0] + pair[1])
                sell_list_list.remove(pair)





    elif Logic.sellLogic() \
            and pair[0] + pair[1] not in sell_list:
        print(sell.delay(pair))
        print(str(datetime.now(pytz.timezone('Africa/Nairobi'))))
        print('****************************************')
        print('****************************************')
        if pair[0] + pair[1] not in sell_list:
            sell_list.append(pair[0] + pair[1])
            sell_list_list.append(pair)
            if pair[0] + pair[1] in buy_list or pair in buy_list_list:
                buy_list.remove(pair[0] + pair[1])
                buy_list_list.remove(pair)
