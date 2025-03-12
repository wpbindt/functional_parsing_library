from dataclasses import dataclass

from functional_parsing_library import Parser
from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.recursive_parser import RecursiveParser
from functional_parsing_library.token_of_type import token_of_type


@dataclass(frozen=True)
class Plus:
    pass


@dataclass(frozen=True)
class Star:
    pass


@dataclass(frozen=True)
class Number:
    value: int


class Expression:
    pass


@dataclass(frozen=True)
class Product(Expression):
    left: Expression
    right: Expression


@dataclass(frozen=True)
class Sum(Expression):
    left: Expression
    right: Expression


@dataclass(frozen=True)
class Literal(Expression):
    value: int


def test_parse_with_non_strings() -> None:
    """
    expression -> sum
    sum -> product & ("+" product)*
    sum -> product "+" sum | product
    product -> literal "*" product | literal
    literal -> NUMBER
    """
    ArithmeticToken = Number | Plus | Star
    literal: Parser[list[ArithmeticToken], Literal] = (lambda n: Literal(n.value)) * token_of_type(Number)
    product: RecursiveParser[list[ArithmeticToken], Expression] = RecursiveParser()
    product.parser = (Product * literal & (token_of_type(Star) > product.parser)) | literal
    sum_: RecursiveParser[list[ArithmeticToken], Expression] = RecursiveParser()
    sum_.parser = (Sum * product.parser & (token_of_type(Plus) > sum_.parser)) | product.parser
    expression = sum_.parser

    tokens: list[ArithmeticToken] = [Number(3), Plus(), Number(4), Star(), Number(5), Plus(), Number(6)]
    expected_result = Sum(left=Literal(3), right=Sum(left=Product(Literal(4), Literal(5)), right=Literal(6)))
    assert_parsing_succeeds(expression, tokens).with_result(expected_result).with_remainder([])
