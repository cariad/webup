"""
**WebUp** is a Python package for uploading websites to Amazon Web Services S3
buckets.

- Uploads files and subdirectories
- Multi-threaded for concurrent parallel uploads
- Sets Cache-Control and Content-Type headers

## Usage

To upload a directory with the default configuration:

```python
from webup import upload

upload("./public", "my-bucket")
```

Some content types are baked-in. To add more content types:

```python
from webup import set_content_type, upload

set_content_type(".foo", "application/foo")
upload("./public", "my-bucket")
```

All files have the Cache-Control value "max-age=60" by default. To configure this:

```python
from webup import set_default_maximum_age, set_maximum_age, upload

# Serve *.css files with Cache-Control "max-age=600":
set_maximum_age(".css", 600)

# Serve all other files with Cache-Control "max-age=300":
set_default_maximum_age(300)

upload("./public", "my-bucket")
```

To perform a dry-run:

```python
from webup import upload

upload("./public", "my-bucket", read_only=True)
```

## Configuration

### Cache-Control headers

By default, every object will be assigned the Cache-Control header "max-age=60".

To set a maximum age per file type, call `set_maximum_age`.

To set the default content type, call `set_default_maximum_age`.

### Content-Type headers

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
