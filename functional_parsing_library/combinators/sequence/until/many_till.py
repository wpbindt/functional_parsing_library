from typing import Any

from functional_parsing_library.combinators.sequence.until.many_till_exclusive import many_till_exclusive
from functional_parsing_library.parser import Parser, U, TokenStream


def many_till(parser: Parser[TokenStream, U], until: Parser[TokenStream, Any]) -> Parser[TokenStream, list[U]]:
    """
    Parses one or more matches for parser, followed by a match for until. Consumes the match for until.
    For example,
    >>> from functional_parsing_library.strings import char
    >>> parser = many_till(char('a'), char('b'))
    >>> parser('aab').result
    ['a', 'a']
    >>> parser('aab').remainder
    ''
    """
    return many_till_exclusive(parser, until) < until
