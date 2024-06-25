from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.strings.char_in import char_in


def test_char_in_fails_on_no_characters_specified() -> None:
    assert_parsing_fails(char_in(''), 'whatever')


def test_char_in_succeeds_on_right_character() -> None:
    assert_parsing_succeeds(char_in('w'), 'w').with_result('w')


def test_char_in_keeps_remainder() -> None:
    assert_parsing_succeeds(char_in('w'), 'whatever').with_remainder('hatever')


def test_char_in_only_parses_one() -> None:
    assert_parsing_succeeds(char_in('i'), 'ii').with_result('i')
