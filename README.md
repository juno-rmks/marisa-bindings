# marisa-bindings

[![CI](https://github.com/juno-rmks/marisa-bindings/actions/workflows/ci.yaml/badge.svg)](https://github.com/juno-rmks/marisa-bindings/actions)
[![PyPI version](https://img.shields.io/pypi/v/marisa-bindings.svg)](https://pypi.org/project/marisa-bindings/)
[![Python versions](https://img.shields.io/pypi/pyversions/marisa-bindings.svg)](https://pypi.org/project/marisa-bindings/)
[![License](https://img.shields.io/pypi/l/marisa-bindings.svg)](LICENSE)

This project provides Python bindings for the MARISA Trie library implemented in C++ using SWIG.

## Installation

Using a virtual environment is recommended to isolate dependencies and avoid conflicts.

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install from PyPI

```bash
pip install marisa-bindings
```

### Install from GitHub

```bash
pip install git+https://github.com/juno-rmks/marisa-bindings.git
```

## Binary Distribution and Source Builds

Prebuilt wheels may be available for selected platforms.

If no compatible wheel is available for your system, pip will automatically build the package from source.

### Requirements for Building from Source

Building from source requires:

- a C++14 compatible compiler
- SWIG (version 4.x recommended)
- Python development headers

Typical compilers by platform:

| Platform | Compiler                         |
| -------- | -------------------------------- |
| Linux    | GCC or Clang                     |
| macOS    | Xcode Command Line Tools         |
| Windows  | MSVC (Visual Studio Build Tools) |

## Usage

Import the module:

```python
from marisa_bindings import marisa
```

For complete usage examples, see:

```
marisa-bindings-sample.py
```

## Vendored Upstream Source

This project vendors the upstream MARISA Trie source code to ensure build reproducibility and long-term stability.

The vendored source is pinned to a specific upstream revision and stored under:

```
third_party/marisa-trie/upstream/
```

The vendoring policy and update procedure are documented in:

```
third_party/marisa-trie/VENDORING.md
```

## License

This project includes code derived from the upstream MARISA Trie project.

Licensing summary:

- Wrapper code: BSD 2-Clause
- Upstream MARISA Trie: BSD 2-Clause OR LGPL 2.1+

See `LICENSE` for full license texts.

## Acknowledgments

Special thanks to the original authors of the MARISA library for their work.
