from dataclasses import dataclass


@dataclass(frozen=True)
class NewLine:
    pass


@dataclass(frozen=True)
class RegularText:
    content: str


@dataclass(frozen=True)
class Header:
    """
    Specified by including
    # something like this on a new line
    in your document
    """
    content: str


@dataclass(frozen=True)
class BoldText:
    """
    Specified by including *something like this* in your document
    """
    content: str


MarkLeftToken = RegularText | Header | BoldText | NewLine
