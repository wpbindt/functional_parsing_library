from asserts import assert_parsing_succeeds
from parsing.combinators.separated_by import separated_by
from parsing.examples.person import Person, Honorific, person
from parsing.parser import Parser
from parsing.strings.char import char

People = list[Person]
UniquePeople = set[Person]


people: Parser[People] = separated_by(person, char(','))
unique_people: Parser[UniquePeople] = set * people


def test_everything() -> None:
    to_parse = ','.join([
        'Mr. Larry David',
        'mr Larry David',
        'ms Susan Sarandon',
        'Mr Conan O\'Brien',
    ])
    assert_parsing_succeeds(people, to_parse).with_result(
        [
            Person('larry', 'david', Honorific.MR),
            Person('larry', 'david', Honorific.MR),
            Person('susan', 'sarandon', Honorific.MS),
            Person('conan', 'o\'brien', Honorific.MR),
        ]
    )


def test_everything_unique() -> None:
    to_parse = ','.join([
        'Mr. Larry David',
        'mr Larry David',
        'ms Susan Sarandon',
        'Mr Conan O\'Brien',
    ])
    assert_parsing_succeeds(unique_people, to_parse).with_result(
        {
            Person('larry', 'david', Honorific.MR),
            Person('susan', 'sarandon', Honorific.MS),
            Person('conan', 'o\'brien', Honorific.MR),
        }
    )
