from parser import Parser


def char_in(string: str) -> Parser[str]:
    def parser(to_parse: str) -> list[tuple[str, str]]:
        if to_parse[0] not in string:
            return []
        return [(to_parse[0], to_parse[1:])]

    return Parser(parser)
