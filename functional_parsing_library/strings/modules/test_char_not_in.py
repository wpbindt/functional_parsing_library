from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.strings.modules.char_not_in import char_not_in


def test_char_not_in_matches_single_character() -> None:
    parser = char_not_in('abcdefg')
    assert_parsing_succeeds(parser, 'h').with_result('h')


def test_char_not_in_does_not_match_specified_character() -> None:
    parser = char_not_in('abcdefg')
    assert_parsing_fails(parser, 'a')


def test_char_not_in_does_not_match_empty_string() -> None:
    parser = char_not_in('adsf')
    assert_parsing_fails(parser, '')
