from functional_parsing_library.parser import Parser, S, T


def ignore_left(left: Parser[T], right: Parser[S]) -> Parser[S]:
    return (lambda t, s: s) * left & right
