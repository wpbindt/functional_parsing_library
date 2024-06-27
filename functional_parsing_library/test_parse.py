import pytest

from functional_parsing_library.parse import parse
from functional_parsing_library.strings import char


def test_parse_parses() -> None:
    my_very_interesting_parser = (lambda x: 'b') * char('a')

    assert parse(my_very_interesting_parser, 'a') == 'b'


def test_raise_error_on_failure_to_parse() -> None:
    with pytest.raises(ValueError):
        parse(char('a'), 'b')


def test_raise_error_on_failure_to_parse_fully() -> None:
    with pytest.raises(ValueError):
        parse(char('b'), 'baaa')
