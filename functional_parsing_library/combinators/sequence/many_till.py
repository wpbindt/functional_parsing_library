from functional_parsing_library.combinators.sequence.many import many
from functional_parsing_library.parser import Parser, U, S


def many_till(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    return many(parser) < until
