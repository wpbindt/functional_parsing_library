from functional_parsing_library.combinators.sequence.some_till_exclusive import some_till_exclusive
from functional_parsing_library.parser import Parser, U, S


def many_till_exclusive(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    """
    Parses one or more matches for parser, followed by a match for until. Does not consume the match for until.
    For example,
    >>> from functional_parsing_library.strings import char
    >>> parser = many_till_exclusive(char('a'), char('b'))
    >>> parser('aab').result
    ['a', 'a']
    >>> parser('aab').remainder
    'b'
    """
    return (lambda t, ts: [t, *ts]) * parser & some_till_exclusive(parser, until)
