from __future__ import annotations
from typing import Any, Generic
from unittest import TestCase

from parser import Parser, T, S


class ParsingTestResult(Generic[S]):
    def __init__(
        self,
        test_case: TestCase,
        actual: tuple[T, str]
    ) -> None:
        self._test_case = test_case
        self._actual = actual

    def with_result(self, expected: S) -> ParsingTestResult[S]:
        self._test_case.assertEqual(self._actual[0], expected)
        return self

    def with_remainder(self, expected: str) -> ParsingTestResult[S]:
        self._test_case.assertEqual(self._actual[1], expected)
        return self


def assert_parsing_succeeds(test_case: TestCase, parser: Parser[Any], to_parse: str) -> ParsingTestResult:
    result = parser(to_parse)
    test_case.assertGreater(len(list(result)), 0)
    return ParsingTestResult(
        test_case=test_case,
        actual=next(iter(result)),
    )


def assert_parsing_fails(test_case: TestCase, parser: Parser[Any], to_parse: str) -> None:
    test_case.assertListEqual(list(parser(to_parse)), [])
