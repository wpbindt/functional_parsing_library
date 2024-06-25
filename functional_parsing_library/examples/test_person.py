from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.examples.person import person, surname, name, honorific, Honorific


def test_parse_person() -> None:
    assert_parsing_succeeds(person, 'Mr. John revelator')


def test_parse_person_parse_lowercase() -> None:
    assert_parsing_succeeds(person, 'Mr. john Revelator')


def test_parse_surname_parses_lowercase_and_no_space() -> None:
    assert_parsing_succeeds(surname, 'john ').with_remainder(' ')


def test_parse_name_parses_uppercase_and() -> None:
    assert_parsing_succeeds(name, 'John ')


def test_parse_mr() -> None:
    assert_parsing_succeeds(honorific, 'Mr. ').with_result(Honorific.MR)


def test_parse_mr_parses_lowercase() -> None:
    assert_parsing_succeeds(honorific, 'mr. ')


def test_parse_ms() -> None:
    assert_parsing_succeeds(honorific, 'Ms. ').with_result(Honorific.MS)


def test_parse_ms_parses_lowercase() -> None:
    assert_parsing_succeeds(honorific, 'ms. ').with_result(Honorific.MS)
