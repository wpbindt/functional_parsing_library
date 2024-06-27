from functional_parsing_library.check_for_empty_string import check_for_empty_string
from functional_parsing_library.parser import Parser, ParseResults, CouldNotParse
from functional_parsing_library.strings.modules.pop_one_character import pop_one_character


def char(c: str) -> Parser[str]:
    """
    Creates a parser which parses a single character c. For example,
    >>> char('a')('aabcd').result
    'a'
    >>> char('a')('aabcd').remainder
    'abcd'
    >>> from functional_parsing_library.parser import CouldNotParse
    >>> isinstance(char('a')('bla'), CouldNotParse)
    True
    """
    @check_for_empty_string
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if to_parse[0] != c:
            return CouldNotParse(f'String "{to_parse}" does not start with "{c}"')

        return pop_one_character(to_parse)

    return Parser(parser)
