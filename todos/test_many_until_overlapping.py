import pytest

from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.combinators import many_till
from functional_parsing_library.strings import char


@pytest.mark.xfail
def test_that_many_till_stops_on_until() -> None:
    a = char('a')
    b = char('b')
    parser = many_till(a | b, a < b)
    assert_parsing_succeeds(parser, 'baab').with_result(['b', 'a']).with_remainder('')
