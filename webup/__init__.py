import importlib.resources

from webup.cache_control import (
    cache_control,
    default_max_age,
    max_age,
    register_max_age,
)
from webup.content_type import content_type, register_content_type

with importlib.resources.open_text(__package__, "VERSION") as t:
    __version__ = t.readline().strip()

__all__ = [
    "cache_control",
    "content_type",
    "default_max_age",
    "max_age",
    "register_content_type",
    "register_max_age",
]
