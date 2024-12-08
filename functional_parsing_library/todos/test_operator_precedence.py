import pytest

from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.strings import char


@pytest.mark.xfail
def test_operator_precedence() -> None:
    a = char('a')
    b = char('b')
    c = char('c')

    assert_parsing_succeeds(a > b < c, 'abc').with_result('b')
