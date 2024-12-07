from functional_parsing_library.parser import Parser, S, CouldNotParse


class ParsingError(Exception):
    pass


def run_parser(parser: Parser[S], to_parse: str) -> S:
    parse_result = parser(to_parse)
    if isinstance(parse_result, CouldNotParse):
        raise ParsingError
    return parse_result.result
