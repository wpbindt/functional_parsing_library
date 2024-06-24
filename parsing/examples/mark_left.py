from dataclasses import dataclass

import pytest

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.combinators.lookahead import lookahead
from parsing.combinators.many import many, some
from parsing.examples.person import const
from parsing.strings.char import char
from parsing.strings.char_not_in import char_not_in


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


MarkLeftToken = RegularText | Header | BoldText | NewLine


SPECIAL_CHARACTERS = '*\n'

normal_character = char_not_in(SPECIAL_CHARACTERS)
normal_words = ''.join * many(normal_character)
regular_text = RegularText * normal_words

new_line = const(NewLine()) * lookahead(char('\n'), char('\n'))

mark_left_token = regular_text | new_line
mark_left = some(mark_left_token)


@pytest.mark.parametrize('special_character', list(SPECIAL_CHARACTERS))
def test_that_regular_text_skips_special_characters(special_character: str) -> None:
    assert_parsing_succeeds(regular_text, f'hi mom{special_character}').with_remainder(special_character)


def test_that_regular_text_parses_to_regular_text() -> None:
    assert_parsing_succeeds(regular_text, 'hi mom').with_result(RegularText('hi mom'))


def test_that_new_line_does_not_parse_single_new_line() -> None:
    assert_parsing_fails(new_line, '\n')


def test_that_new_line_parses_double_new_line_and_consumes_only_one() -> None:
    assert_parsing_succeeds(new_line, '\n\n').with_result(NewLine()).with_remainder('\n')


def test_that_mark_left_parses_no_text() -> None:
    assert_parsing_succeeds(mark_left, '').with_result([])


def test_that_mark_left_parses_some_text() -> None:
    to_parse = 'hi mom\n\n'
    expected = [
        RegularText('hi mom'),
        NewLine(),
    ]
    assert_parsing_succeeds(mark_left, to_parse).with_result(expected)
