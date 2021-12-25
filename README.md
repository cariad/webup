# WebUp

**WebUp** is a Python package for uploading websites to Amazon Web Services S3 buckets.

**WebUp** uploads directories recursively and sets Cache-Control and Content-Type HTTP headers.

**Full documentation is online at [cariad.github.io/webup](https://cariad.github.io/webup/webup.html).**

## Installation

```bash
pip install webup
```

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

**Full documentation is online at [cariad.github.io/webup](https://cariad.github.io/webup/webup.html).**

## Licence

WebUp is released at [github.com/cariad/webup](https://github.com/cariad/webup) under the MIT Licence.

See [LICENSE](https://github.com/cariad/webup/blob/main/LICENSE) for more information.

## Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance DevOps and backend engineer. My contact details are available on my personal wiki at [cariad.earth](https://cariad.earth).

Please consider supporting my open source projects by [sponsoring me on GitHub](https://github.com/sponsors/cariad/).
