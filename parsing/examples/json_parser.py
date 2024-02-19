import string
import unittest

from asserts import assert_parsing_succeeds
from parsing.combinators.separated_by import some_separated_by
from parsing.examples.integer import integer
from parsing.parser import Parser
from parsing.recursive_parser import RecursiveParser
from parsing.strings.char import char
from parsing.strings.word import word

valid_json_string_chars = string.ascii_letters + 'I don\'t actually know what JSON allows'
json_string: Parser[str] = ...

_json = RecursiveParser()
array = (char('[') > some_separated_by(_json.parser, word(', '))) < char(']')
_json.parser = integer | array
json = _json.parser
"""
This one is a bit difficult, since it's a parser for a recursive language. 

Since the specification of json is self-referential, we have to do some ugly
things involving the RecursiveParser class to avoid NameErrors (you cannot 
write something like JSON = integer | ((char('[') > JSON) < char(']')), that's 
super illegal)

Try extending the json parser to be able to parse json strings, and then
json objects
"""


class TestJSONParsing(unittest.TestCase):
    def test_integer(self) -> None:
        assert_parsing_succeeds(self, json, '3').with_result(3)

    def test_string(self) -> None:
        assert_parsing_succeeds(self, json_string, '"hi"').with_result('hi')

    def test_empty_array(self) -> None:
        assert_parsing_succeeds(self, json, '[]').with_result([])

    def test_array_with_integer(self) -> None:
        assert_parsing_succeeds(self, json, '[3]')

    def test_array_with_multiple_integers(self) -> None:
        assert_parsing_succeeds(self, json, '[3, 4]')

    def test_nested_array(self) -> None:
        assert_parsing_succeeds(self, json, '[3, []]').with_result([3, []])

    def test_empty_object(self) -> None:
        assert_parsing_succeeds(self, json, '{}').with_result({})

    def test_object_with_one_item(self) -> None:
        assert_parsing_succeeds(self, json, '{"a": 3}').with_result({'a': 3})

    def test_object_with_two_items(self) -> None:
        assert_parsing_succeeds(self, json, '{"a": 3, "b": 4}').with_result({'a': 3, 'b': 4})
