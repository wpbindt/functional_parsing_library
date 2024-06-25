from functional_parsing_library.parser import Parser, T, S, ParseResults, CouldNotParse


def or_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[T | S]:
    def parser(to_parse: str) -> ParseResults[T | S] | CouldNotParse:
        try_1 = parser_1(to_parse)
        if not isinstance(try_1, CouldNotParse):
            return try_1
        return parser_2(to_parse)

    return Parser(parser)
