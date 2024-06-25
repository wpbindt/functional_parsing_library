from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.combinators.lookahead import lookahead
from functional_parsing_library.combinators.sequence.many import many
from functional_parsing_library.parser import Parser, U, S
from functional_parsing_library.strings.word import word


def many_till_exclusive(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    return lookahead(many(parser), look_for=until)


def test_that_many_till_exclusive_matches_many_and_keeps_remainder() -> None:
    assert_parsing_succeeds(many_till_exclusive(word('a'), word('b')), 'aab').with_result(['a', 'a']).with_remainder('b')


def test_that_many_till_exclusive_fails_on_nothing() -> None:
    assert_parsing_fails(many_till_exclusive(word('a'), word('b')), 'b')


def test_that_many_till_exclusive_fails_when_lookahead_fails() -> None:
    assert_parsing_fails(many_till_exclusive(word('a'), word('b')), 'a')
