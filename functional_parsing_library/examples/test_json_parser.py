from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.examples.json_parser import json, json_string


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


def test_object_with_object_value() -> None:
    assert_parsing_succeeds(json, '{"a": {"b": 4}}').with_result({'a': {'b': 4}})
