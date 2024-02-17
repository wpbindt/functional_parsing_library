from __future__ import annotations

from typing import Any, Generic
from unittest import TestCase

from parsing.parser import Parser, S, CouldNotParse, ParseResults


class ParsingTestResult(Generic[S]):
    def __init__(
        self,
        test_case: TestCase,
        actual: ParseResults[S],
    ) -> None:
        self._test_case = test_case
        self._actual = actual

    def with_result(self, expected: S) -> ParsingTestResult[S]:
        self._test_case.assertEqual(self._actual.result, expected)
        return self

    def with_remainder(self, expected: str) -> ParsingTestResult[S]:
        self._test_case.assertEqual(self._actual.remainder, expected)
        return self


def assert_parsing_succeeds(test_case: TestCase, parser: Parser[Any], to_parse: str) -> ParsingTestResult:
    result = parser(to_parse)
    test_case.assertNotIsInstance(result, CouldNotParse)
    assert not isinstance(result, CouldNotParse)
    return ParsingTestResult(
        test_case=test_case,
        actual=result,
    )


def assert_parsing_fails(test_case: TestCase, parser: Parser[Any], to_parse: str) -> None:
    test_case.assertEqual(
        parser(to_parse),
        CouldNotParse(),
    )
