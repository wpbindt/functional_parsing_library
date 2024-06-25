from __future__ import annotations

import unittest

from functional_parsing_library.hacky_function_composition import o, _Composer


class TestComposition(unittest.TestCase):
    def test_composing_two_functions_works(self) -> None:
        plus_2 = lambda x: x + 2
        times_9 = lambda x: x * 9

        composed = plus_2 /o/ times_9

        self.assertEqual(composed(3), 29)

    def test_composing_three_functions_works(self) -> None:
        o = _Composer()

        plus_2 = lambda x: x + 2

        composed = plus_2 /o/ plus_2 /o/ plus_2

        self.assertEqual(composed(3), 9)

    def test_composing_four_functions_works(self) -> None:
        o = _Composer()

        plus_2 = lambda x: x + 2

        composed = plus_2 /o/ plus_2 /o/ plus_2 /o/ plus_2

        self.assertEqual(composed(3), 11)
