from string import ascii_lowercase as ascii_lowercase_letters, ascii_uppercase as ascii_uppercase_letters

import pytest

from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library import ascii_lowercase, ascii_uppercase, ascii_letter


@pytest.mark.parametrize('lowercase_letter', ascii_lowercase_letters)
def test_ascii_lowercase_matches_lowercase_ascii(lowercase_letter: str) -> None:
    assert_parsing_succeeds(ascii_lowercase, lowercase_letter).with_result(lowercase_letter)


@pytest.mark.parametrize('uppercase_letter', ascii_uppercase_letters)
def test_ascii_lowercase_does_not_match_uppercase_ascii(uppercase_letter: str) -> None:
    assert_parsing_fails(ascii_lowercase, uppercase_letter)


@pytest.mark.parametrize('lowercase_letter', ascii_lowercase_letters)
def test_ascii_uppercase_does_not_match_lowercase_ascii(lowercase_letter: str) -> None:
    assert_parsing_fails(ascii_uppercase, lowercase_letter)


@pytest.mark.parametrize('uppercase_letter', ascii_uppercase_letters)
def test_ascii_letter_matches_uppercase_ascii(uppercase_letter: str) -> None:
    assert_parsing_succeeds(ascii_letter, uppercase_letter).with_result(uppercase_letter)


@pytest.mark.parametrize('lowercase_letter', ascii_lowercase_letters)
def test_ascii_letter_matches_lowercase_ascii(lowercase_letter: str) -> None:
    assert_parsing_succeeds(ascii_letter, lowercase_letter).with_result(lowercase_letter)
