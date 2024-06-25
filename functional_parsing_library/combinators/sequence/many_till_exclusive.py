from functional_parsing_library.combinators.lookahead import lookahead
from functional_parsing_library.combinators.sequence.many import many
from functional_parsing_library.parser import Parser, U, S


def many_till_exclusive(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    return lookahead(many(parser), look_for=until)
