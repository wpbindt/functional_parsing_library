import string
from typing import Any

from asserts import assert_parsing_succeeds
from parsing.combinators.many import many
from parsing.combinators.separated_by import some_separated_by
from parsing.integer.integer import integer
from parsing.recursive_parser import RecursiveParser
from parsing.strings.char import char
from parsing.strings.char_in import char_in
from parsing.strings.word import word


valid_json_string_chars = string.ascii_letters + 'idk'
json_string = ''.join * ((char('"') > many(char_in(valid_json_string_chars))) < char('"'))

_json: RecursiveParser[Any] = RecursiveParser()
array = (char('[') > some_separated_by(_json.parser, word(', '))) < char(']')
key_value_pair = (lambda t, s: (t, s)) * (json_string < word(': ')) & _json.parser
json_object = dict * (
    (char('{') > some_separated_by(key_value_pair, word(', '))) < char('}')
)
_json.parser = integer | array | json_string | json_object
json = _json.parser


def test_integer() -> None:
    assert_parsing_succeeds(json, '3').with_result(3)


def test_string() -> None:
    assert_parsing_succeeds(json_string, '"hi"').with_result('hi')


def test_empty_array() -> None:
    assert_parsing_succeeds(json, '[]').with_result([])


def test_array_with_integer() -> None:
    assert_parsing_succeeds(json, '[3]')


def test_array_with_multiple_integers() -> None:
    assert_parsing_succeeds(json, '[3, 4]')


def test_nested_array() -> None:
    assert_parsing_succeeds(json, '[3, []]').with_result([3, []])


def test_empty_object() -> None:
    assert_parsing_succeeds(json, '{}').with_result({})


def test_object_with_one_item() -> None:
    assert_parsing_succeeds(json, '{"a": 3}').with_result({'a': 3})


def test_object_with_two_items() -> None:
    assert_parsing_succeeds(json, '{"a": 3, "b": 4}').with_result({'a': 3, 'b': 4})
