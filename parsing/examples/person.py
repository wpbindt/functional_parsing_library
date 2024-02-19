from __future__ import annotations

import unittest
from dataclasses import dataclass
from enum import Enum

from asserts import assert_parsing_succeeds
from parsing.parser import Parser


class Honorific(Enum):
    MR = 0
    MS = 1


@dataclass(frozen=True)
class Person:
    name: str
    surname: str
    honorific: Honorific

    @classmethod
    def from_tuple(cls, tuple_: tuple[Honorific, str, str]) -> Person:
        return Person(
            name=tuple_[1],
            surname=tuple_[2],
            honorific=tuple_[0],
        )


honorific: Parser[Honorific] = ...
name: Parser[str] = ...
person: Parser[Person] = ...

cases = [
    ('Mr. Larry David', Person('larry', 'david', Honorific.MR)),
    ('mr Larry David', Person('larry', 'david', Honorific.MR)),
    ('ms Susan Sarandon', Person('susan', 'sarandon', Honorific.MS)),
    ('Mr Conan O\'Brien', Person('conan', 'o\'brien', Honorific.MR)),
]


class TestPersonParsing(unittest.TestCase):
    def test_everything(self) -> None:
        for to_parse, parsed in cases:
            with self.subTest(to_parse):
                assert_parsing_succeeds(self, person, to_parse).with_result(parsed).with_remainder('')
