from parser import Parser, ParseResults


def char_in(string: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str]:
        if to_parse[0] not in string:
            return []
        return [(to_parse[0], to_parse[1:])]

    return Parser(parser)
