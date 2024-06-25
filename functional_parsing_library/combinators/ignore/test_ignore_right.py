from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.strings.modules.word import word


def test_that_ignore_right_parses_both_and_returns_left() -> None:
    left = word('(This I want)')
    right = word('(This I ignore)')

    assert_parsing_succeeds(left < right, '(This I want)(This I ignore)').with_result('(This I want)').with_remainder('')
