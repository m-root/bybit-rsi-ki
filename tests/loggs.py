import logging
from datetime import date
from pathlib import Path
today = date.today()

my_file = Path("./logs/{}.log".format(today.strftime("%d %B %Y")))
if my_file.is_file():
	pass
else:
	logging.getLogger("./logs/{}.log".format(today.strftime("%d %B %Y")))


logging.basicConfig(filename="./logs/{}.log".format(today.strftime("%d %B %Y")),
					format='%(asctime)s %(message)s',
					)

#Creating an object
logger=logging.getLogger()


logger.setLevel(logging.DEBUG)



def debug_debug(message):
		return logger.debug(message)

def debug_info(message):
	return logger.info(message)

def debug_warning(message):
	return logger.warning(message)


def debug_error(message):
	return logger.error(message)

def debug_critical(message):
	return logger.critical(message)

#
# debug_debug('Ujanja pale chini')
# debug_info('Ujanja pale chini')
# debug_warning('Ujanja pale chini')
# debug_error('Ujanja pale chini')
# debug_critical(debug_error('Ujanja pale chini'))
