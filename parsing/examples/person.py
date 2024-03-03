import string
from enum import auto, Enum
from typing import Callable, Any

from asserts import assert_parsing_succeeds
from parsing.combinators.many import many
from parsing.parser import S
from parsing.strings.char import char
from parsing.strings.char_in import char_in
from parsing.strings.word import word


class Honorific(Enum):
    MR = auto()
    MS = auto()


class Person:
    def __init__(self, honorific: Honorific, name: str, surname: str) -> None:
        self._honorific = honorific
        self._name = name
        self._surname = surname


def const(value: S) -> Callable[[Any], S]:
    return lambda x: value


alphabetic_character = char_in(string.ascii_letters)
alphabetic_word = ''.join * many(alphabetic_character)
mr = const(Honorific.MR) * (word('Mr.') | word('mr.'))
ms = const(Honorific.MS) * (word('Ms.') | word('ms.'))
honorific = (mr | ms) < char(' ')
name = alphabetic_word < char(' ')
surname = alphabetic_word
person = Person * honorific & name & surname


def test_parse_person() -> None:
    assert_parsing_succeeds(person, 'Mr. John revelator')


def test_parse_person_parse_lowercase() -> None:
    assert_parsing_succeeds(person, 'Mr. john Revelator')


def test_parse_surname_parses_lowercase_and_no_space() -> None:
    assert_parsing_succeeds(surname, 'john ').with_remainder(' ')


def test_parse_name_parses_uppercase_and() -> None:
    assert_parsing_succeeds(name, 'John ')


def test_parse_mr() -> None:
    assert_parsing_succeeds(honorific, 'Mr. ').with_result(Honorific.MR)


def test_parse_mr_parses_lowercase() -> None:
    assert_parsing_succeeds(honorific, 'mr. ')


def test_parse_ms() -> None:
    assert_parsing_succeeds(honorific, 'Ms. ').with_result(Honorific.MS)


def test_parse_ms_parses_lowercase() -> None:
    assert_parsing_succeeds(honorific, 'ms. ').with_result(Honorific.MS)
