from functional_parsing_library import Parser, digit, n_times, many
from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.fmap import to_int


def test_that_bind_can_be_used_to_construct_context_dependent_parsers() -> None:
    input_ = str(12_3456_71234567)
    expected_output = [2, 456, 1234567]

    def make_block_parser(digits: int) -> Parser[str, int]:
        return to_int * (''.join * n_times(digits, str * digit))

    parser = many(digit >> make_block_parser)

    assert_parsing_succeeds(parser, input_).with_result(expected_output)
