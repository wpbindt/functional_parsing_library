from collections.abc import Container

from functional_parsing_library.parser import Parser
from functional_parsing_library.strings.char_does_not_match import char_does_not_match
from functional_parsing_library.strings.char_in import char_in


def char_not_in(characters: Container[str]) -> Parser[str]:
    return char_does_not_match(char_in(characters))
