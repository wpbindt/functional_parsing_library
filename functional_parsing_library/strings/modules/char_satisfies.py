from typing import Callable

from functional_parsing_library.check_for_empty_string import check_for_empty_string
from functional_parsing_library.parser import Parser, ParseResults, CouldNotParse
from functional_parsing_library.strings.modules.pop_one_character import pop_one_character


def char_satisfies(condition: Callable[[str], bool]) -> Parser[str]:
    """
    Match any character satisfying the given condition. For example,
    >>> char_satisfies(lambda c: c == 'b')('b').result
    'b'
    """
    @check_for_empty_string
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if condition(to_parse[0]):
            return pop_one_character(to_parse)
        return CouldNotParse()
    return Parser(parser)
