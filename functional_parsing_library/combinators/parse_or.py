from functional_parsing_library.parser import Parser, T, S, ParseResults, CouldNotParse, TokenStream


def or_2(parser_1: Parser[TokenStream, T], parser_2: Parser[TokenStream, S]) -> Parser[TokenStream, T | S]:
    """
    Combines two parsers into one which tries to match for the first one, and upon failure match for the second one.
    The `|` operator is overloaded to call this function. For example,
    >>> from functional_parsing_library.strings import char
    >>> parser = char('a') | char('b')
    >>> parser('a').result
    'a'
    >>> parser('b').result
    'b'
    """
    def parser(to_parse: TokenStream) -> ParseResults[TokenStream, T | S] | CouldNotParse:
        try_1 = parser_1(to_parse)
        if not isinstance(try_1, CouldNotParse):
            return try_1
        return parser_2(to_parse)

    return Parser(parser)
