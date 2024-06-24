from dataclasses import dataclass

import pytest

from asserts import assert_parsing_succeeds
from parsing.combinators.many import many
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


MarkLeftToken = RegularText | NewLine | Header | BoldText


SPECIAL_CHARACTERS = '*\n'

normal_character = char_not_in(SPECIAL_CHARACTERS)
normal_words = ''.join * many(normal_character)
regular_text = RegularText * normal_words


@pytest.mark.parametrize('special_character', list(SPECIAL_CHARACTERS))
def test_that_regular_text_skips_special_characters(special_character: str) -> None:
    assert_parsing_succeeds(regular_text, f'hi mom{special_character}').with_remainder(special_character)


def test_that_regular_text_parses_to_regular_text() -> None:
    assert_parsing_succeeds(regular_text, f'hi mom').with_result(RegularText('hi mom'))
