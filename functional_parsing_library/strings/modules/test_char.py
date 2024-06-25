from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.strings.modules.char import char


def test_that_empty_strings_do_not_parse() -> None:
    assert_parsing_fails(char('h'), '').with_reason('String to parse is empty')


def test_that_parsing_a_different_character_fails() -> None:
    h_parser = char('h')
    assert_parsing_fails(h_parser, 'peep').with_reason('String "peep" does not start with "h"')


def test_that_parsing_h_succeeds() -> None:
    h_parser = char('h')
    assert_parsing_succeeds(h_parser, 'h').with_result('h')


def test_that_parsing_h_with_remainder_gives_remainder() -> None:
    h_parser = char('h')
    assert_parsing_succeeds(h_parser, 'hoi').with_remainder('oi')
