import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def real_world_bad_example():
    """
    WoW it fixed in Python 3!
    """
    try:
        1 / 0
    except ZeroDivisionError:
        try:
            send_message_to_somebody()
        except NameError:
            pass
        logging.exception('We have a problem :-/')


def real_world_good_example():
    try:
        1 / 0
    except ZeroDivisionError:
        real_exc_info = sys.exc_info()
        try:
            send_message_to_somebody()
        except NameError:
            logging.debug('send message failed', exc_info=True)
        logging.error('We have a problem :-/', exc_info=real_exc_info)


def exc_scope():
    print(sys.exc_info(), '0'*30)
    try:
        print(sys.exc_info(), '1'*30)
        1 / 0
    except ZeroDivisionError:
        print(sys.exc_info(), '2'*30)
        try:
            print(sys.exc_info(), '3'*30)
            send_message_to_somebody()
        except NameError:
            print(sys.exc_info(), '4'*30)
        print(sys.exc_info(), '5'*30)
    print(sys.exc_info(), '6'*30)
