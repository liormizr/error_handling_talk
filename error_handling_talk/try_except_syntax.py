""" https://docs.python.org/3.6/tutorial/errors.html """
from . import include


@include
def pass_example():
    try:
        print('Doing work')
    except:
        print('will handle Errors')
    else:
        print('will handle success')
    finally:
        print('will run in the end')


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
