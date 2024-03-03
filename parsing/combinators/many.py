from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, T, ParseResults, CouldNotParse
from parsing.strings.char import char


def some(parser: Parser[T]) -> Parser[list[T]]:
    def parser_(to_parse: str) -> ParseResults[list[T]]:
        remainder = to_parse
        result: list[T] = []
        while remainder:
            one_parse = parser(remainder)
            if isinstance(one_parse, CouldNotParse):
                break
            result.append(one_parse.result)
            remainder = one_parse.remainder

        return ParseResults(result=result, remainder=remainder)

    return Parser(parser_)


def many(parser: Parser[T]) -> Parser[list[T]]:
    return (lambda t, ts: [t, *ts]) * parser & some(parser)


def test_some_parses_one() -> None:
    parser = some(char('a'))

    assert_parsing_succeeds(parser, 'a').with_result(['a'])


def test_some_parses_more() -> None:
    parser = some(char('a'))

    assert_parsing_succeeds(parser, 'aa').with_result(['a', 'a'])


def test_some_parses_none() -> None:
    parser = some(char('a'))

    assert_parsing_succeeds(parser, 'h').with_result([]).with_remainder('h')


def test_many_fails_to_parse_unparsable() -> None:
    parser = many(char('a'))

    assert_parsing_fails(parser, 'b')


def test_many_parses_one() -> None:
    parser = many(char('a'))

    assert_parsing_succeeds(parser, 'a').with_result(['a'])


def test_many_parses_two() -> None:
    parser = many(char('a'))

    assert_parsing_succeeds(parser, 'aa').with_result(['a', 'a'])
