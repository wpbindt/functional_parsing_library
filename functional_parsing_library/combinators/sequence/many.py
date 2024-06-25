from functional_parsing_library.parser import Parser, T, ParseResults, CouldNotParse


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
