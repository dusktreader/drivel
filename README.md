[![Build Status](https://github.com/dusktreader/drivel/actions/workflows/push.yaml/badge.svg)](https://github.com/dusktreader/drivel/actions/workflows/push.yaml)
[![PyPI Versions](https://img.shields.io/pypi/v/py-drivel?style=plastic&label=pypi-version)](https://img.shields.io/pypi/v/py-drivel?style=plastic&label=pypi-version)

> [!IMPORTANT]
> I'm looking for a job right now! If you know of any openings that match my skill-set,
> please let me know! You can read my resume over at my
> [cv site](https://cv.dusktreader.dev). Thanks!!

# Drivel

[//]: # (Add an asciicast)

`drivel` is a package and CLI application to provide you with
[metasyntactic](https://en.wikipedia.org/wiki/Metasyntactic_variable) name values.

It is heavily inspired by the [metasyntactic](https://github.com/ask/metasyntactic) package. However, `metasyntactic`
is quite old and it is unmaintained.

Drivel is a modern package that borrows many of the themes from `metasyntactic`, used others for inspiratoin, and adds a
few new ones.


## Quickstart

### Install `drivel`:

```bash
pip install py-drivel
```

### CLI

#### [Optional] Configure `drivel`:

To see all the configuration options, run:

```bash
drivel config --help
```

The simplest working config would look like this:

```bash
drivel config bind --default-theme=star-wars
```

#### Run `drivel`:

To get 10 metasyntactic names from the default theme, run:

```bash
drivel give 10
```


### Package

Just import in your code, and go!

```python
from drivel.themes import Theme

print(Theme.load().give())
```

## Configuration

The `drivel` CLI stores its configuration in a file so that it can use
the same settings for many runs without having a super-cluttered command line. You can
check out the location where the config file is saved in the `config.py` module.

[//]: # (Add documentation for the config subcommands here in the vein of smart-letters)
[//]: # (Add documentation for the other subcommands here in the vein of smart-letters)


## License

Distributed under the MIT License. See `LICENSE.md` for more information.
