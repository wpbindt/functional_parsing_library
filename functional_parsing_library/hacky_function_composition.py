from __future__ import annotations

import unittest
from typing import Callable, TypeVar, Generic

U = TypeVar('U')
T = TypeVar('T')
S = TypeVar('S')


class _Composer:
    def __rtruediv__(self, other: Callable[[T], S]) -> _LeftAppliedComposer[T, S]:
        return _LeftAppliedComposer(other)


class _LeftAppliedComposer(Generic[T, S]):
    def __init__(self, function: Callable[[T], S]):
        self._function = function

    def __truediv__(self, other: Callable[[U], T]) -> Callable[[U], S]:
        return lambda u: self._function(other(u))

    def __call__(self, arg: T) -> S:
        return self._function(arg)


o = _Composer()


class TestComposition(unittest.TestCase):
    def test_composing_two_functions_works(self) -> None:
        plus_2 = lambda x: x + 2
        times_9 = lambda x: x * 9

        composed = plus_2 /o/ times_9

        self.assertEqual(composed(3), 29)

    def test_composing_three_functions_works(self) -> None:
        o = _Composer()

        plus_2 = lambda x: x + 2

        composed = plus_2 /o/ plus_2 /o/ plus_2

        self.assertEqual(composed(3), 9)

    def test_composing_four_functions_works(self) -> None:
        o = _Composer()

        plus_2 = lambda x: x + 2

        composed = plus_2 /o/ plus_2 /o/ plus_2 /o/ plus_2

        self.assertEqual(composed(3), 11)
