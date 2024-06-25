from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.strings.word import word


def test_that_parsing_a_different_character_fails() -> None:
    hoi_parser = word('hoi')
    assert_parsing_fails(hoi_parser, 'subaru').with_reason('String "subaru" does not start with "hoi"')


def test_that_parsing_h_succeeds() -> None:
    hoi_parser = word('hoi')
    assert_parsing_succeeds(hoi_parser, 'hoi').with_result('hoi').with_remainder('')


def test_that_parsing_h_with_remainder_gives_remainder() -> None:
    hoi_parser = word('hoi')
    assert_parsing_succeeds(hoi_parser, 'hoi hoi').with_remainder(' hoi')
