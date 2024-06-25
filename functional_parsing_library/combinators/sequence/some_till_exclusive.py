from functional_parsing_library.combinators.lookahead import lookahead
from functional_parsing_library.combinators.sequence.many import some
from functional_parsing_library.parser import Parser, U, S


def some_till_exclusive(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    return lookahead(some(parser), look_for=until)
