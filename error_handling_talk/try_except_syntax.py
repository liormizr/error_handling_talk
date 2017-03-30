""" https://docs.python.org/3.6/tutorial/errors.html """
import sys
from . import include


@include
def pass_example():
    try:
        # Doing work
        sys.stdout.write('Fat ')
        sys.stdout.flush()
    except:
        # Will Handle Errors
        sys.stdout.write('monkey ')
        sys.stdout.flush()
    else:
        # Will Handle Success
        sys.stdout.write('chicken ')
        sys.stdout.flush()
    finally:
        # Will Run in the End
        sys.stdout.write('lips ')
        sys.stdout.flush()


@include
def error_example1():
    try:
        1 / 0
    except (ZeroDivisionError, ValueError):
        print('handle ZeroDivisionError errors')
    except:
        print('handle any Exception')


@include
def error_example2():
    try:
        1 / 0
    except Exception:
        print('handle any Exception')
    except ZeroDivisionError:
        print('handle ZeroDivisionError errors')
