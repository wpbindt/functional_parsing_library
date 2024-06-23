import string
from dataclasses import dataclass

from asserts import assert_parsing_succeeds
from parsing.combinators.many import some, many
from parsing.examples.person import const
from parsing.strings.char_in import char_in
from parsing.strings.word import word


@dataclass(frozen=True)
class RegularText:
    content: str


@dataclass(frozen=True)
class NewLine:
    pass


MarkLeft = list[RegularText | NewLine]

allowed_characters = ' ' + string.ascii_letters
allowed_character = char_in(allowed_characters)
new_line = const(NewLine()) * word('\n')
regular_text = (RegularText * (''.join * many(allowed_character))) < word('\n')
mark_left_token = regular_text | new_line
mark_left = some(mark_left_token)


def test_that_nothing_is_parsed() -> None:
    assert_parsing_succeeds(mark_left, '').with_result([])


def test_that_regular_text_gets_parsed_to_regular_text() -> None:
    assert_parsing_succeeds(mark_left, 'hi there\n').with_result([RegularText('hi there')])


def test_that_new_lines_are_parsed_as_such() -> None:
    input_ = 'hi there\n\nthis is another paragraph\n'
    expected = [
        RegularText('hi there'),
        NewLine(),
        RegularText('this is another paragraph'),
    ]
    assert_parsing_succeeds(mark_left, input_).with_result(expected).with_remainder('')
