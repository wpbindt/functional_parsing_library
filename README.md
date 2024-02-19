In this kata, you will implement a fully-fledged functional parsing library. Each module contains a number of tests which
you're expected to turn green, but no one is stopping you from writing your own as well.

Some tips:
    - Running mypy helps, even though the output will start out pretty messy. 
      `grep -v ellipsis | grep -v empty-body` helps a bit
    - Combinators are not always as commutative (a|b == b|a) or associative ((a*b)*c == a*(b*c)) as they seem,
      and they might not satisfy the distribution laws you expect. Parentheses are your friend!

Implement the basic building blocks for parsers in the modules (in order)
    - `parsing.strings.char`
    - `parsing.strings.word`
    - `parsing.strings.char_in`

Move on to implementing the `combinators` module. You do not need to implement everything here, but try to do `fmap` first,
and then `and_2` and the ignore functions. The `many` and `some` functions are probably the most difficult in this section.

After a while, move on to `parsing.examples`, and implement the modules there. `digit` is the easiest, and `json_parser`
is the hardest.
