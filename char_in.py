from parser import Parser, ParseResults, CouldNotParse


def char_in(string: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if to_parse[0] not in string:
            return CouldNotParse()
        return ParseResults(to_parse[0], to_parse[1:])

    return Parser(parser)
