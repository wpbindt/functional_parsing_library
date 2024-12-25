import pytest

from functional_parsing_library import run_parser, ParsingError, NotFullyParsed, char


def test_run_parser_returns_parse_result_when_successful() -> None:
    parser = char('a')
    assert run_parser(parser, 'ab') == 'a'


def test_run_parser_raises_exception_when_failing_to_parse() -> None:
    parser = char('b')
    with pytest.raises(ParsingError):
        run_parser(parser, 'a')


def test_run_parser_raises_exception_when_remainder() -> None:
    parser = char('a')
    with pytest.raises(NotFullyParsed):
        run_parser(parser, 'ab', raise_on_remainder=True)
