from collections.abc import Container

from functional_parsing_library.check_for_empty_string import check_for_empty_string
from functional_parsing_library.parser import Parser, ParseResults, CouldNotParse
from functional_parsing_library.strings.modules.pop_one_character import pop_one_character


def char_in(string: Container[str]) -> Parser[str]:
    @check_for_empty_string
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if to_parse[0] not in string:
            return CouldNotParse()

        return pop_one_character(to_parse)

    return Parser(parser)
