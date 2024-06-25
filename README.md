# functional_parsing_library

A small production non-ready Python library implementing basic applicative parsers. Roughly speaking, these are functions
with signature `str -> T | CouldNotParse` transforming strings into structured data. For example, you might have a function
`integer` which will transform `"1"` and `"-1919"` to the integers `1` and `-1919`, and the string `"boink"` to `CouldNotParse()`.

What makes these functions useful is that they can be combined with so-called parser combinators. For example, if we 
already have parsers `nonnegative_integer` and `negative_integer`, the `integer` parser from earlier could be written as 
`integer = nonnegative_integer | negative_integer`. This library implements various such combinators, such as `many`, 
`some`, `ignore_left`, `many_till`, and so on.

Another piece of structure that makes these functions useful is that they're functorial: If I have a parser `p` of type 
`Parser[T]` (that is, a function which parses strings to objects of type `T`), and a function `f: T -> S`, then `f * p`
will be a parser for objects of type `S`. For example, take `len * many(word('borf'))`, and try to parse `"borfborfborf"`.
Here `word('borf')` will parse `"borf"` to the string `"borf"` (and any other string to `CouldNotParse`), so the parser
`many(word('borf')` will try and match as many `"borf"`s as possible and parse our string to the list `['borf', 'borf', 'borf']`. 
The length of this list is 3, so `len * many(word('borf'))` parses our string to the integer 3.

This works with multi-argument functions as well. If `f` is a function of type `[T, S] -> U`, and we have parsers `p`
and `q` for objects of type `T` and `S`, then `f * p & q` will first try to match `p`, and if this succeeds it will try
and match `q`, and finally it will apply `f`.
