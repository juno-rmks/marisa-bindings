# marisa-bindings

This is an unofficial project that provides Python bindings for the MARISA
Trie, which is implemented in C++ using SWIG.

## Installation

It is recommended to use a Python virtual environment to isolate dependencies
and avoid conflicts. To create and activate a virtual environment, run:

```console
% python -m venv .venv
% . .venv/bin/activate
```

### Installing from PyPI

To install `marisa-bindings` from PyPI into your virtual environment, run:

```console
% pip install marisa-bindings
```

### Installing from GitHub

Alternatively, if you prefer to install `marisa-bindings` directly from
the GitHub repository, use:

```console
% pip install git+https://github.com/juno-rmks/marisa-bindings.git
```

## Usage

To get started with `marisa_bindings`, import the `marisa` module, which
provides access to the MARISA trie functionalities:

```python
from marisa_bindings import marisa
```

For more detailed usage examples, refer to the [`marisa-bindings-sample.py`](marisa-bindings-sample.py) file.

## License

This project is licensed under the following terms:

- **Wrapped Code**: The wrapped code in this repository is licensed under
  the BSD 2-Clause License.
- **Original marisa-trie Code**: The original marisa-trie code is dual-licensed
  under the BSD 2-Clause License and the LGPL 2.1 or any later version.

For more details, please see the [LICENSE](LICENSE) file.

## Acknowledgments

Special thanks to the original authors of the MARISA library for their work.
