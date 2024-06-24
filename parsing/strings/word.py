from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, ParseResults, CouldNotParse


def word(word_to_parse_for: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if not to_parse.startswith(word_to_parse_for):
            return CouldNotParse(f'String "{to_parse}" does not start with "{word_to_parse_for}"')
        return ParseResults(word_to_parse_for, to_parse[len(word_to_parse_for):])

    return Parser(parser)


def test_that_parsing_a_different_character_fails() -> None:
    hoi_parser = word('hoi')
    assert_parsing_fails(hoi_parser, 'subaru').with_reason('String "subaru" does not start with "hoi"')


def test_that_parsing_h_succeeds() -> None:
    hoi_parser = word('hoi')
    assert_parsing_succeeds(hoi_parser, 'hoi').with_result('hoi').with_remainder('')


def test_that_parsing_h_with_remainder_gives_remainder() -> None:
    hoi_parser = word('hoi')
    assert_parsing_succeeds(hoi_parser, 'hoi hoi').with_remainder(' hoi')
