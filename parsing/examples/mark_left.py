from asserts import assert_parsing_succeeds
from parsing.combinators.many import some

MarkLeft = list

mark_left_token = ...
mark_left = some(mark_left_token)


def test_that_nothing_is_parsed() -> None:
    assert_parsing_succeeds(mark_left, '').with_result([])
