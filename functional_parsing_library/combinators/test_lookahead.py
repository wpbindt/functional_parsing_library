from typing import cast

from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.combinators.lookahead import lookahead
from functional_parsing_library.parser import CouldNotParse
from functional_parsing_library.strings.word import word


def test_that_lookahead_looks_ahead() -> None:
    parser = lookahead(word('a'), look_for=word('b'))

    assert_parsing_succeeds(parser, 'ab').with_result('a')


def test_that_lookahead_fails_when_lookahead_not_ahead() -> None:
    parser = lookahead(word('a'), look_for=word('b'))
    expected_failure_message = cast(CouldNotParse, word('b')('')).reason

    assert_parsing_fails(parser, 'a').with_reason(expected_failure_message)


def test_that_lookahead_keeps_remainder() -> None:
    parser = lookahead(word('a'), look_for=word('b'))

    assert_parsing_succeeds(parser, 'ab').with_remainder('b')
