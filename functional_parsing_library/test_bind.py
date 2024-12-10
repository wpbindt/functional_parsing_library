from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.bind_parser import bind
from functional_parsing_library.combinators import many
from functional_parsing_library.combinators.sequence.n_times_parser import n_times
from functional_parsing_library.fmap import to_int
from functional_parsing_library.parser import Parser
from functional_parsing_library.strings import digit


def test_acceptance() -> None:
    """

    Language to parse:
    valid input is any string of digits
    one token consists of a positive single-digit number specifying the length n of the block,
    followed by n characters forming an n-digit number

    """

    def make_block_parser(digits: int) -> Parser[int]:
        return to_int * (''.join * n_times(digits, str * digit))

    parser = many(bind(digit, make_block_parser))

    input_ = str(12_3456_71234567)
    expected_output = [2, 456, 1234567]

    assert_parsing_succeeds(parser, input_).with_result(expected_output)
