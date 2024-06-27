from functional_parsing_library.parser import Parser, S, CouldNotParse


def parse(parser: Parser[S], to_parse: str) -> S:
    result = parser(to_parse)
    if isinstance(result, CouldNotParse):
        raise ValueError
    if len(result.remainder) > 0:
        raise ValueError
    return result.result
