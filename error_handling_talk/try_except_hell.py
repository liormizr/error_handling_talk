""" Life - working a lot with ty except in Python """
from . import include


@include
def example1():
    def _hell():
        try:
            print('Doing work')
            return 0
        except:
            print('will handle Errors')
            return 1
        else:
            print('will handle success')
            return 2
        finally:
            print('will run in the end')
            return 3
    print(_hell())


@include
def example2():
    def _hell():
        try:
            print('Doing work')
            1 / 0
            return 0
        except ZeroDivisionError:
            print('will handle Errors')
            return 1
        else:
            print('will handle success')
            return 2
        finally:
            print('will run in the end')
            return 3
    print(_hell())


@include
def example3():
    def _hell():
        try:
            print('Doing work')
            return 0
        except ZeroDivisionError:
            print('will handle Errors')
            return 1
        else:
            print('will handle success')
            return 2
    print(_hell())


@include
def example4():
    def _hell():
        try:
            print('Doing work')
            1 / 0
            return 0
        except ValueError:
            return 1
        except ArithmeticError:
            return 2
        except ZeroDivisionError:
            return 3
        except TypeError:
            return 4
        except:
            return 5
    print(_hell())
