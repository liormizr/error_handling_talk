from collections import OrderedDict


def include(example):
    suite = example.__module__.split('.')[-1]
    talk_map.setdefault(suite, {'examples': []})
    talk_map[suite]['examples'].append(example)
    return example
talk_map = OrderedDict()

from . import try_except_syntax
from . import try_except_log
from . import try_except_hell
from . import try_except_with_context_manager

talk_map['try_except_syntax']['sources'] = try_except_syntax.__doc__
talk_map['try_except_log']['sources'] = try_except_log.__doc__
talk_map['try_except_hell']['sources'] = try_except_hell.__doc__
talk_map['try_except_with_context_manager']['sources'] = try_except_with_context_manager.__doc__
