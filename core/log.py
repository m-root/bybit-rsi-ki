import logging
from datetime import date
from pathlib import Path

today = date.today()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
my_file = Path("../logs/{}.log".format(today.strftime("%d-%B-%Y")))
if my_file.is_file():
    pass
else:
    logging.getLogger("../logs/{}.log".format(today.strftime("%d-%B-%Y")))


logging.basicConfig(filename="./logs/{}.log".format(today.strftime("%d-%B-%Y")),
                    format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
                    )


def for_settings():
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../logs/{}.log".format(today.strftime("%d-%B-%Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../logs/{}.log".format(today.strftime("%d-%B-%Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d-%B-%Y")),
                        format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging


def debug_debug(message):
    return for_settings().debug(message)


def debug_info(message):
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../logs/{}.log".format(today.strftime("%d-%B-%Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../logs/{}.log".format(today.strftime("%d-%B-%Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d-%B-%Y")),
                        format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.info(message)


def debug_warning(message):
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../logs/{}.log".format(today.strftime("%d-%B-%Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../logs/{}.log".format(today.strftime("%d-%B-%Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d-%B-%Y")),
                        format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.warning(message)


''' Converts the cross balance in the API to the base value equivalence for buy purposes'''


def debug_error(message):
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../logs/{}.log".format(today.strftime("%d-%B-%Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../logs/{}.log".format(today.strftime("%d-%B-%Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d-%B-%Y")),
                        format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.error(message)


''' Converts the cross balance in the API to the base value equivalence for buy purposes'''


def debug_critical(message):
    today = date.today()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_file = Path("../logs/{}.log".format(today.strftime("%d-%B-%Y")))
    if my_file.is_file():
        pass
    else:
        logging.getLogger("../logs/{}.log".format(today.strftime("%d-%B-%Y")))

    logging.basicConfig(filename="../logs/{}.log".format(today.strftime("%d-%B-%Y")),
                        format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
                        )
    return logging.critical(message)

# # # #
# debug_debug('Ujanja pale chini')
# debug_info('Ujanja pale chini')
# debug_warning('Ujanja pale chini')
# debug_error('Ujanja pale chini')
# debug_critical(debug_error('Ujanja pale chini'))


#
# import logging
# from datetime import date
# from pathlib import Path
#
# def get_project_root() -> Path:
#     return Path(__file__).parent.parent
#
# def fileNameLocation():
#     today = date.today()
#     return ('{}/logs/{}.log'.format(get_project_root().parent, today.strftime("%d-%B-%Y")))
#
#
# def fileCheck():
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#     my_file = Path(fileNameLocation())
#     if my_file.is_file():
#         pass
#     else:
#         logging.getLogger(fileNameLocation())
#
#     logging.basicConfig(filename=fileNameLocation(),
#                         format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
#                         )
#     return logging
#
#
#
#
# def debug_debug(message):
#     logging.basicConfig(filename=fileNameLocation(),
#                         format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
#                         )
#
#     return logging.debug(message)
#
#
# ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
#
#
# def debug_info(message):
#     logging.basicConfig(filename=fileNameLocation(),
#                         format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
#                         )
#     return logging.info(message)
#
#
# ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
#
#
# def debug_warning(message):
#     fileCheck()
#     logging.basicConfig(filename=fileNameLocation(),
#                         format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
#                         )
#     return logging.warning(message)
#
#
# ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
#
#
# def debug_error(message):
#     fileCheck()
#     logging.basicConfig(filename=fileNameLocation(),
#                         format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
#                         )
#     return logging.error(message)
#
#
# ''' Converts the cross balance in the API to the base value equivalence for buy purposes'''
#
#
# def debug_critical(message):
#     logging.basicConfig(filename=fileNameLocation(),
#                         format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s'
#                         )
#     return logging.critical(message)
