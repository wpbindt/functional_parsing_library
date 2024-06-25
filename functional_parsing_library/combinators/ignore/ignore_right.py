from functional_parsing_library.parser import Parser, S, T


def ignore_right(left: Parser[T], right: Parser[S]) -> Parser[T]:
    return (lambda t, s: t) * left & right
