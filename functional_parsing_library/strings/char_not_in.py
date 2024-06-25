from collections.abc import Container

from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.parser import Parser
from functional_parsing_library.strings.char_does_not_match import char_does_not_match
from functional_parsing_library.strings.char_in import char_in


def char_not_in(characters: Container[str]) -> Parser[str]:
    return char_does_not_match(char_in(characters))


def test_char_not_in_matches_single_character() -> None:
    parser = char_not_in('abcdefg')
    assert_parsing_succeeds(parser, 'h').with_result('h')


def test_char_not_in_does_not_match_specified_character() -> None:
    parser = char_not_in('abcdefg')
    assert_parsing_fails(parser, 'a')


def test_char_not_in_does_not_match_empty_string() -> None:
    parser = char_not_in('adsf')
    assert_parsing_fails(parser, '')
