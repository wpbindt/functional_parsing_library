from functional_parsing_library.parser import Parser, S, U, ParseResults, CouldNotParse


def lookahead(parser: Parser[S], look_for: Parser[U]) -> Parser[S]:
    def parser_(to_parse: str) -> ParseResults[S] | CouldNotParse:
        result_combined = (parser < look_for)(to_parse)
        if isinstance(result_combined, CouldNotParse):
            return result_combined
        return parser(to_parse)

    return Parser(parser_)
