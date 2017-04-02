#!/usr/bin/env python
"""
Error Handling Hints & Tricks

Usage:
  talk.py --version
  talk.py (-h | --help)
  talk.py start
  talk.py try_except_syntax
  talk.py try_except_log
  talk.py try_except_hell
  talk.py try_except_with_context_manager

Options:
  --version     Show talk version.
  -h --help     Show talk menu and examples.
"""
import sys
import logging
import inspect
from functools import partial

from docopt import docopt

from IPython import embed, get_ipython
from IPython.core.autocall import ExitAutocall
from IPython.terminal.ipapp import load_default_config

from error_handling_talk import talk_map

_ipython_config = load_default_config()
_ipython_config.InteractiveShellEmbed = _ipython_config.TerminalInteractiveShell
_ipython_config.TerminalInteractiveShell.banner1 = ''
_ipython_config.TerminalInteractiveShell.banner2 = '\x1b[2J\x1b[H'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def _run_all():
    for example_suite_name, suite in talk_map.items():
        _run_suite(example_suite_name, suite)


def _run_suite(suite_name, suite):
    for index, example in enumerate(suite['examples']):
        Next = ExitAutocall()
        globals().update({
            example.__name__: example,
            'python2': partial(_run_in_python2, example),
        })
        embed(
            header=_create_header(suite_name, suite, index, example),
            config=_ipython_config)


def _create_header(suite_name, suite, index, example):
    return '\n'.join((
        '| {}:'.format(suite_name.title()),
        '| Sources: {}'.format(suite['sources']),
        '|',
        '| {suite} - {index}. '.format(suite=suite_name, index=index + 1),
        _code_example(example),
        '| What will happen? >> {0.__name__}(), What will happen in python2? >> python2()'.format(example),
        "| Press 'Next' to go to the next example",
    ))


def _code_example(example):
    return '\n'.join(
        '|    >> ' + line
        for line in inspect.getsource(example).splitlines()
    )


def _run_in_python2(example):
    shell = get_ipython()
    code_string = '\n'.join(inspect.getsource(example).splitlines()[1:])
    call = (
        'import sys\n'
        'import logging\n'
        'logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)\n'
    )
    call += code_string
    call += '\n{0.__name__}()'.format(example)
    shell.run_cell_magic('python2', '', call)


if __name__ == '__main__':
    talk_options = docopt(__doc__, version='0.0.1')
    try:
        if talk_options['start']:
            _run_all()
            sys.exit(0)
        for suite_name, show in talk_options.items():
            if show:
                _run_suite(suite_name, talk_map[suite_name])
    except (KeyboardInterrupt, SystemExit):
        print()
    print('Goodbye')
