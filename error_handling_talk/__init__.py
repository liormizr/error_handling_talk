from collections import OrderedDict

from . import try_except_syntax
from . import try_except_log

talk_map = OrderedDict()
talk_map['try_except_syntax'] = {
    'examples': [
        try_except_syntax.pass_example,
        try_except_syntax.error_example1,
        try_except_syntax.error_example2,
    ],
    'sources': try_except_syntax.__doc__,
}
talk_map['try_except_log'] = {
    'examples': [
        try_except_log.basic_example,
        try_except_log.real_world_bad_example,
        try_except_log.real_world_good_example,
        try_except_log.python3_example,
    ],
    'sources': try_except_log.__doc__
}