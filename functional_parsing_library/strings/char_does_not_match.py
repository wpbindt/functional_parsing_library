from functional_parsing_library.check_for_empty_string import check_for_empty_string
from functional_parsing_library.parser import U, Parser, ParseResults, CouldNotParse
from functional_parsing_library.strings.pop_one_character import pop_one_character


def char_does_not_match(parser: Parser[U]) -> Parser[str]:
    @check_for_empty_string
    def parser_(to_parse: str) -> ParseResults[str] | CouldNotParse:
        result = parser(to_parse)
        if not isinstance(result, CouldNotParse):
            return CouldNotParse()

        return pop_one_character(to_parse)

    return Parser(parser_)


