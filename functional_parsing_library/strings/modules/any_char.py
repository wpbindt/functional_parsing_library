from functional_parsing_library.check_for_empty_string import check_for_empty_string
from functional_parsing_library.parser import CouldNotParse, Parser, ParseResults
from functional_parsing_library.strings.modules.pop_one_character import pop_one_character


@check_for_empty_string
def _any_char(to_parse: str) -> ParseResults[str] | CouldNotParse:
    return pop_one_character(to_parse)


any_char = Parser(_any_char)
