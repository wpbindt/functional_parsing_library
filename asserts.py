from __future__ import annotations

from typing import Any, Generic

from parsing.parser import Parser, S, CouldNotParse, ParseResults


class _ParsingSuccessTestResult(Generic[S]):
    def __init__(
        self,
        actual: ParseResults[S],
    ) -> None:
        self._actual = actual

    def with_result(self, expected: S) -> _ParsingSuccessTestResult[S]:
        assert self._actual.result == expected
        return self

    def with_remainder(self, expected: str) -> _ParsingSuccessTestResult[S]:
        assert self._actual.remainder == expected
        return self


def assert_parsing_succeeds(parser: Parser[S], to_parse: str) -> _ParsingSuccessTestResult[S]:
    result = parser(to_parse)
    assert not isinstance(result, CouldNotParse)
    return _ParsingSuccessTestResult(
        actual=result,
    )


def assert_parsing_fails(parser: Parser[Any], to_parse: str) -> None:
    assert parser(to_parse) == CouldNotParse()
