import time
from configparser import ConfigParser
parser = ConfigParser()
# parser.read('.test/dev.ini')
# parser.read('/home/m-root/PycharmProjects/novatron/dev.ini')

while True:
    parser.read('/home/m-root/PycharmProjects/novatron/tests/dev.ini')
    print(parser.get('mysql_conn_data', 'host'))
    time.sleep(2)
