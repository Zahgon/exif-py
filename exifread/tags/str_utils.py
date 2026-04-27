"""
Misc utilities.
"""


def make_string_uc(seq) -> str:
    """
    Special version to deal with the code in the first 8 bytes of a user comment.
    First 8 bytes gives coding system e.g. ASCII vs. JIS vs Unicode.
    """
    pass


def make_string(seq) -> str:
    """
    Don't throw an exception when given an out of range character.
    """
    pass
