from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.strings.modules.char import char
from functional_parsing_library.strings.modules.char_does_not_match import char_does_not_match


def test_parser_matches_stuff_not_matching_parser() -> None:
    parser = char_does_not_match(char('a'))

    assert_parsing_succeeds(parser, 'b').with_result('b')


def test_parser_does_not_match_parser() -> None:
    parser = char_does_not_match(char('a'))

    assert_parsing_fails(parser, 'a')
