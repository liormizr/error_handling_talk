""" https://docs.python.org/3.6/library/logging.html """
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def basic_example():
    try:
        1 / 0
    except ZeroDivisionError:
        exception_type, exception_instance, traceback = sys.exc_info()
        logging.error(
            'We have a problem :-/',
            exc_info=(exception_type, exception_instance, traceback))
    # Same as:
    print('~'*30)
    try:
        1 / 0
    except ZeroDivisionError:
        logging.error('We have a problem :-/', exc_info=True)
    # Same as:
    print('~'*30)
    try:
        1 / 0
    except ZeroDivisionError:
        logging.exception('We have a problem :-/')


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


def python3_example():
    def foo():
        try:
            bar()
        except NameError as error:
            raise ValueError('Chain errors') from error

    try:
        foo()
    except ValueError:
        logging.exception('Chain error traceback')
