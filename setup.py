from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from webup import __version__

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Internet :: WWW/HTTP :: Site Management",
    "Typing :: Typed",
]

if "a" in __version__:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in __version__:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Uploads websites to Amazon Web Services S3 buckets",
    include_package_data=True,
    install_requires=[
        "boto3~=1.20",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="webup",
    packages=[
        "webup",
        "webup.models",
    ],
    package_data={
        "webup": ["py.typed"],
        "webup.models": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/webup",
    version=__version__,
)
