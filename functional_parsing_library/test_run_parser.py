import pytest

from functional_parsing_library.run_parser import run_parser, ParsingError
from functional_parsing_library.strings import char


def test_run_parser_returns_parse_result_when_successful() -> None:
    parser = char('a')
    assert run_parser(parser, 'a') == 'a'


def test_run_parser_raises_exception_when_failing_to_parse() -> None:
    parser = char('b')
    with pytest.raises(ParsingError):
        run_parser(parser, 'a')
