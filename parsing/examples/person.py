from __future__ import annotations

import string
from dataclasses import dataclass
from enum import Enum
from typing import Callable

from asserts import assert_parsing_succeeds
from parsing.combinators.many import many
from parsing.combinators.parse_and import and_
from parsing.parser import Parser, T
from parsing.strings.char import char
from parsing.strings.char_in import char_in
from parsing.strings.word import word


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

def const(value: T) -> Callable[[], T]:
    return lambda x: value

mr = const(Honorific.MR) * (word('Mr.') | word('mr') | word('Mr'))
ms = const(Honorific.MS) * word('ms')

honorific: Parser[Honorific] = (mr | ms) < char(' ')
name: Parser[str] = (lambda s: s.lower()) * (''.join * many(char_in(string.ascii_letters) | char("'")))
person: Parser[Person] = Person.from_tuple * and_(honorific, name, (char(' ') > name))

cases = [
    ('Mr. Larry David', Person('larry', 'david', Honorific.MR)),
    ('mr Larry David', Person('larry', 'david', Honorific.MR)),
    ('ms Susan Sarandon', Person('susan', 'sarandon', Honorific.MS)),
    ('Mr Conan O\'Brien', Person('conan', 'o\'brien', Honorific.MR)),
]


def test_everything() -> None:
    for to_parse, parsed in cases:
        assert_parsing_succeeds(person, to_parse).with_result(parsed).with_remainder('')
