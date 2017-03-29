""" https://docs.python.org/3/library/contextlib.html """
import logging

from . import include


@include
def suppress_example():
    from contextlib import suppress

    with suppress(ZeroDivisionError):
        1 / 0

    # Same Like
    try:
        1 / 0
    except ZeroDivisionError:
        pass

    class _suppress:
        def __init__(self, *exceptions):
            self._exceptions = exceptions

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_val, exc_tb):
            return exc_type is not None and issubclass(exc_type, self._exceptions)


@include
def context_manager_example():
    from contextlib import suppress

    class ErrorMessage(suppress):
        def __init__(self, *exceptions, logger=logging.getLogger()):
            self.logger = logger
            super().__init__(*exceptions)

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                self.logger.exception('We have a problem :-/')
            return super().__exit__(exc_type, exc_val, exc_tb)

    with ErrorMessage(ZeroDivisionError):
        1 / 0
