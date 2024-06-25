from __future__ import annotations

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


