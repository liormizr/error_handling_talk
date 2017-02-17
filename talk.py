"""
Error Handling Hints & Tricks

Usage:
  talk.py --version
  talk.py (-h | --help)
  talk.py start
  talk.py try_except_syntax
  talk.py try_except_log

Options:
  --version     Show talk version.
  -h --help     Show talk menu and examples.
"""
import sys
import inspect

from docopt import docopt

from error_handling_talk import talk_map


def _run_suite(suite_name, suite):
    for index, example in enumerate(suite['examples']):
        sys.stdout.write('\x1b[2J\x1b[H')
        print('{}:'.format(suite_name.title()))
        print('Sources:')
        print('{}'.format(suite['sources']))
        print()
        print('{suite} - {index}. '.format(suite=suite_name, index=index + 1))
        print(inspect.getsource(example))
        input('What will happen? >> {0.__name__}()'.format(example))
        example()
        input('Next?...')


def _run_all():
    for example_suite_name, suite in talk_map.items():
        _run_suite(example_suite_name, suite)


if __name__ == '__main__':
    talk_options = docopt(__doc__, version='0.0.1')
    try:
        if talk_options['start']:
            _run_all()
        for suite_name, show in talk_options.items():
            if show:
                _run_suite(suite_name, talk_map[suite_name])
    except KeyboardInterrupt:
        print()
        print('Goodbye')
