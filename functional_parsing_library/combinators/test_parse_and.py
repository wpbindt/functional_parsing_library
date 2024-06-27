from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.strings.modules.char import char


def test_parse_and_deals_with_callables() -> None:
    def plus(left: str, right: str) -> str:
        return f'{left} plus {right}'

    a = char('a')
    b = char('b')
    parser = plus * a & b
    assert_parsing_succeeds(parser, 'abc').with_result('a plus b').with_remainder('c')


def test_parse_and_deals_with_callables_with_more_arguments() -> None:
    def plus(left: str, middle: str, right: str) -> str:
        return f'{left} plus {middle} plus {right}'

    a = char('a')
    b = char('b')
    c = char('c')
    parser = plus * a & b & c
    assert_parsing_succeeds(parser, 'abc').with_result('a plus b plus c')
