###  Telegram Crypto Signals Bot
Starting celery for multi-core processing for Telegram Crypto Signals Bot     
```
celery -A m_run.crypto_signals.m_core worker --loglevel=info --concurrency=10 -n worker1.%h

```
###  Novatron Signals Bot
Starting celery for multi-core processing for Telegram Crypto Signals Bot     
```
celery -A m_run.novatron_signals.m_core worker --loglevel=info --concurrency=10 -n worker1.%h

```
###  Novatron Signals Bot
Starting celery for multi-core processing for Telegram Crypto Signals Bot     
```
 sudo virtualenv -p python3 venv  
 sudo pip install -r requirements.txt  

```

###  Novatron Bot
Starting celery for multi-core processing Novatron Bot
```
celery -A m_run.novatron.m_core worker --loglevel=info  --concurrency=10 -n worker1.%h

```

###  Trend_Trader Bot

Starting celery for multi-core processing Trendtrader Bot

```
celery -A m_run.trend_trader.m_core worker --loglevel=info  --concurrency=10 -n worker1.%h

```


###  Novatron Bitmex Bot

Starting celery for multi-core processing Trendtrader Bot

```
celery -A m_run.novatron_bitmex.m_core worker --loglevel=info  --concurrency=10 -n worker1.%h

```

