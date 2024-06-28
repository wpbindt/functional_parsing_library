from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.strings.modules.char_satisfies import char_satisfies


def test_char_satisfies_true_matches_any_character() -> None:
    parser = char_satisfies(lambda x: True)
    assert_parsing_succeeds(parser, 'a').with_result('a')


def test_char_satisfies_false_does_not_match_character() -> None:
    parser = char_satisfies(lambda x: False)
    assert_parsing_fails(parser, 'a')


def test_char_satisfies_fails_on_empty_string() -> None:
    parser = char_satisfies(lambda x: True)
    assert_parsing_fails(parser, '')


def test_char_satisfies_applies_condition_to_first_character_only() -> None:
    parser = char_satisfies(lambda x: len(x) == 2)
    assert_parsing_fails(parser, 'ab')
