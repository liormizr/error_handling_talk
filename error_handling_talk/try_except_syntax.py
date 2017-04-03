""" https://docs.python.org/3.6/tutorial/errors.html """
import sys
from . import include


@include
def pass_example():
    try:
        # Doing work
        sys.stdout.write('Fat ')
    except:
        # Will Handle Errors
        sys.stdout.write('monkey ')
    else:
        # Will Handle Success
        sys.stdout.write('chicken ')
    finally:
        # Will Run in the End
        sys.stdout.write('lips ')
    sys.stdout.flush()


@include
def error_example1():
    try:
        1 / 0
    except (ZeroDivisionError, ValueError):
        print('handle ZeroDivisionError')
    except:
        print('handle any Exception')


@include
def error_example2():
    try:
        1 / 0
    except Exception:
        print('handle any Exception')
    except ZeroDivisionError:
        print('handle ZeroDivisionError')


@include
def exc_scope():
    """
    sys.exc_info: 
        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
    exc_info() -> (exc_type, exc_val, exc_tb)
    """
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
