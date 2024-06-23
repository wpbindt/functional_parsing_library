import string
from dataclasses import dataclass

from asserts import assert_parsing_succeeds
from parsing.combinators.many import some, many
from parsing.strings.char_in import char_in


@dataclass(frozen=True)
class RegularText:
    content: str


MarkLeft = list[RegularText]

allowed_characters = ' ' + string.ascii_letters
allowed_character = char_in(allowed_characters)
mark_left_token = RegularText * (''.join * many(allowed_character))
mark_left = some(mark_left_token)


def test_that_nothing_is_parsed() -> None:
    assert_parsing_succeeds(mark_left, '').with_result([])


def test_that_regular_text_gets_parsed_to_regular_text() -> None:
    assert_parsing_succeeds(mark_left, 'hi there').with_result([RegularText('hi there')])
