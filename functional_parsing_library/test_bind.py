from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.bind_parser import bind
from functional_parsing_library.combinators import many
from functional_parsing_library.combinators.sequence.n_times_parser import n_times
from functional_parsing_library.fmap import to_int
from functional_parsing_library.parser import Parser
from functional_parsing_library.strings import digit


def test_that_bind_can_be_used_to_construct_context_dependent_parsers() -> None:
    input_ = str(12_3456_71234567)
    expected_output = [2, 456, 1234567]

    def make_block_parser(digits: int) -> Parser[int]:
        return to_int * (''.join * n_times(digits, str * digit))

    parser = many(bind(digit, make_block_parser))

    assert_parsing_succeeds(parser, input_).with_result(expected_output)
