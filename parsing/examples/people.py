import unittest

from asserts import assert_parsing_succeeds
from parsing.examples.person import Person, Honorific
from parsing.parser import Parser

People = list[Person]
UniquePeople = set[People]


people: Parser[People] = ...
unique_people: Parser[UniquePeople] = ...


class TestPeople(unittest.TestCase):
    def test_everything(self) -> None:
        to_parse = ','.join([
            'Mr. Larry David',
            'mr Larry David',
            'ms Susan Sarandon',
            'Mr Conan O\'Brien',
        ])
        assert_parsing_succeeds(self, people, to_parse).with_result(
            [
                Person('larry', 'david', Honorific.MR),
                Person('larry', 'david', Honorific.MR),
                Person('susan', 'sarandon', Honorific.MS),
                Person('conan', 'o\'brien', Honorific.MR),
            ]
        )

    def test_everything_unique(self) -> None:
        to_parse = ','.join([
            'Mr. Larry David',
            'mr Larry David',
            'ms Susan Sarandon',
            'Mr Conan O\'Brien',
        ])
        assert_parsing_succeeds(self, unique_people, to_parse).with_result(
            {
                Person('larry', 'david', Honorific.MR),
                Person('susan', 'sarandon', Honorific.MS),
                Person('conan', 'o\'brien', Honorific.MR),
            }
        )
