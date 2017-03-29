""" https://docs.python.org/3.6/tutorial/errors.html """
import sys
from . import include


@include
def pass_example():
    try:
        sys.stdout.write('Fat ')
        sys.stdout.flush()
    except:
        sys.stdout.write('monkey ')
        sys.stdout.flush()
    else:
        sys.stdout.write('chicken ')
        sys.stdout.flush()
    finally:
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
