from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.strings.modules.char import char


def test_parsing_neither_fails() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_fails(parser, 'c')


def test_parsing_first_succeeds() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_succeeds(parser, 'a').with_result('a')


def test_parsing_second_succeeds() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_succeeds(parser, 'b').with_result('b')


def test_that_remainder_remains() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_succeeds(parser, 'bingo').with_remainder('ingo')
