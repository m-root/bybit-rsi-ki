import telegram
from celery import Celery

app = Celery('tasks', broker='amqp://')

@app.task(name='telegram_message_relay')
def telegram_message_relay(settings, telegram_message):
    status = settings.bot.send_message(
        chat_id = settings.chat_id,
        text = telegram_message,
        parse_mode = telegram.ParseMode.HTML
    )
    return status

@app.task(name='telegram_print')
def telegram_print( pair, trade_logic, trade_logic_1, trade_logic_2):
    telegram_message = 'PAIR \t: {} \n' \
                       'HASHI FAST CANDLE CLOSE DATA \t: {} \n' \
                       'HASHI SLOW CANDLE CLOSE DATA \t: {} \n' \
                       'MOVING AVERAGE CLOSE DATA \t: {} \n' \
        .format(
        pair,
        trade_logic,
        trade_logic_1,
        trade_logic_2
    )

    # print(self.telegram_message(telegram_message))

@app.task(name='on_screen_print')
def on_screen_print(pair, trade_logic, trade_logic_1, trade_logic_2):
    screen_print = 'PAIR \t: {} \n' \
                   'HASHI FAST CANDLE CLOSE DATA \t: {} \n' \
                   'HASHI SLOW CANDLE CLOSE DATA \t: {} \n' \
                   'MOVING AVERAGE CLOSE DATA \t: {} \n' \
        .format(
        pair,
        trade_logic,
        trade_logic_1,
        trade_logic_2
    )

    print(screen_print)
