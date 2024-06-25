from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.fmap import to_int
from functional_parsing_library.parser import CouldNotParse
from functional_parsing_library.strings.modules.char import char


def test_that_fmap_still_fails_to_parse_unparsable_stuff() -> None:
    parser = to_int * char('3')

    assert_parsing_fails(parser, 'h')


def test_that_fmap_passes_on_failure_reason() -> None:
    parse_to_map_over = char('3')
    parser = to_int * parse_to_map_over
    to_parse = 'h'
    inner_result = parse_to_map_over(to_parse)
    assert isinstance(inner_result, CouldNotParse)
    inner_reason = inner_result.reason

    assert_parsing_fails(parser, to_parse).with_reason(inner_reason)


def test_that_fmap_successfully_parses_parsable_stuff() -> None:
    parser = to_int * char('3')

    assert_parsing_succeeds(parser, '3')


def test_that_fmap_maps_parsed_stuff() -> None:
    parser = to_int * char('3')

    assert_parsing_succeeds(parser, '3').with_result(3)


def test_with_a_different_function() -> None:
    parser = (lambda x: x + 90) * (to_int * char('3'))

    assert_parsing_succeeds(parser, '3').with_result(93)
