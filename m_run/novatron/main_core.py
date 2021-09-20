from celery import Celery
from kombu import Exchange, Queue
from payload.payload import Payload
from datetime import datetime
from m_run.novatron import settings

from celery import bootsteps


buy_list = []
sell_list = []

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
    # backend='redis://localhost:6379/0'
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

app.conf.task_queues = (default_queue, )

# Add steps to workers that declare DLX and DLQ if they don't exist
app.steps['worker'].add(DeclareDLXnDLQ)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key


currentTime = datetime.utcnow().strftime("%M")

# pairs = settings.pairs
pair = 'BTCUSDT'



@app.task
def buy(pair):
    if pair not in buy_list:

        # buy_list.append(pair)
        # if pair in sell_list:
        #     sell_list.remove(pair)

        payload = Payload(pair=settings.pair, time_frame = settings.period, chat_id = settings.chat_id, file_path = settings.bot, settings = settings)
        payload.buy_logic()

        if pair not in buy_list:
            buy_list.append(pair)
            if pair in sell_list:
                sell_list.remove(pair)

@app.task
def sell(pair):
    if pair not in sell_list:
        # if pair in buy_list:
        #     buy_list.remove(pair)
        #     sell_list.append(pair)

        payload = Payload(pair=settings.pair, time_frame = settings.period, chat_id = settings.chat_id, file_path = settings.bot, settings = settings)
        payload.sell_logic()

        if pair not in sell_list:
            sell_list.append(pair)
            if pair in buy_list:
                buy_list.remove(pair)




# @app.task
def logic(pair):
    buy.delay(pair)
    sell.delay(pair)






'''
celery -A m_run.crypto_signals.main worker --loglevel=info

'''
# sell.delay(pair='BTCUSDT', time_frame=settings.time_frame, chat_id=settings.chat_id, settings=settings)
# sell.delay()

'''
@app.task
def add(x, y):
    return x + y


@app.task(acks_late=True)
def div(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError as exc:
        raise Reject(exc, requeue=False)
'''


# result_backend = 'db+sqlite:///results.sqlite'
# # app = Celery('tasks', backend=result_backend, broker='amqp://')
# app = Celery('tasks', broker='amqp://')
# @app.task
#
#
# @app.task
# def main():
#
#     # while True:
#     buy.delay()
#     sell.delay()
#
#
#
# #
# if __name__ == '__main__':
#     main.delay()
#


