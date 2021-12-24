"""
**WebUp** is a Python package for uploading files to Amazon Web Services S3
buckets.

**WebUp** uploads directories recursively, and sets Cache-Control and
Content-Type HTTP headers ready for serving on the web.

## Default Cache-Control headers

By default, every object will be assigned the Cache-Control header "max-age=60".

To set a maximum age per file type, call `set_maximum_age`.

To set the default content type, call `set_default_maximum_age`.

## Default Content-Type headers

| Filename&nbsp; | Content-Type                 |
|----------------|------------------------------|
| .css           | text/css                     |
| .eot           | application/vnd.m-fontobject |
| .html          | text/html                    |
| .js            | text/javascript              |
| .png           | image/png                    |
| .ttf           | font/ttf                     |
| .woff          | font/woff                    |
| .woff2         | font/woff2                   |
| *              | application/octet-stream     |
| &nbsp;         |                              |

To add additional content types, call `set_content_type`.

To set the default content type, call `set_default_content_type`.


## Example

```python
from webup import set_default_maximum_age, upload

# CSS file caches should expire after 10 minutes:
add_maximum_age(".css", 600)

# All other cached files should expire after 5 minutes:
set_default_maximum_age(300)

# Perform a dry-run upload of the ./public directory to "my-bucket":
upload("./public", "my-bucket", read_only=True)

# Now *really* upload it:
upload("./public", "my-bucket")
```
"""

import importlib.resources

from webup.cache_control import set_default_maximum_age, set_maximum_age
from webup.content_type import set_content_type, set_default_content_type
from webup.queue import upload

with importlib.resources.open_text(__package__, "VERSION") as t:
    __version__ = t.readline().strip()

__all__ = [
    # This is intentionally the first so it's at the top of the API
    # documentation.
    "upload",
    "set_default_content_type",
    "set_default_maximum_age",
    "set_content_type",
    "set_maximum_age",
]
