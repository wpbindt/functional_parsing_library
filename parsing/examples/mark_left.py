from dataclasses import dataclass

from asserts import assert_parsing_succeeds
from parsing.combinators.many_till_exclusive import many_till_exclusive
from parsing.strings.any_char import any_char
from parsing.strings.word import word


@dataclass(frozen=True)
class NewLine:
    pass


@dataclass(frozen=True)
class RegularText:
    content: str


@dataclass(frozen=True)
class Header:
    """
    Specified by including
    # something like this on a new line
    in your document
    """
    content: str


@dataclass(frozen=True)
class BoldText:
    """
    Specified by including *something like this* in your document
    """
    content: str


MarkLeftToken = RegularText | NewLine | Header | BoldText


SPECIAL_CHARACTERS = '#*\n'


regular_text = many_till_exclusive(any_char, word('\n'))


def test_that_regular_text_parses_until_new_line_exclusive() -> None:
    assert_parsing_succeeds(regular_text, 'hi mom\n').with_remainder('\n')
