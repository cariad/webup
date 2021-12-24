from typing import Dict

from webup.suffix import normalize_suffix

_max_ages: Dict[str, int] = {}

default_max_age = 60
"""
Default maximum age in seconds.
"""


def cache_control(suffix: str) -> str:
    """
    Gets the Cache-Control header for a type of file.

    Arguments:
        suffix: Filename suffix.
    """

    return f"max-age={max_age(suffix)}"


def max_age(suffix: str) -> int:
    """
    Gets the maximum age in seconds for a type of file.

    Arguments:
        suffix: Filename suffix.
    """

    suffix = normalize_suffix(suffix)
    return _max_ages.get(suffix, default_max_age)


def register_max_age(suffix: str, max_age: int) -> None:
    """
    Registers the maximum age of a type of file.

    Arguments:
        suffix: Filename suffix.
    """

    suffix = normalize_suffix(suffix)
    _max_ages[suffix] = max_age
