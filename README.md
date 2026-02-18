# marisa-bindings

[![CI](https://github.com/juno-rmks/marisa-bindings/actions/workflows/ci.yaml/badge.svg)](https://github.com/juno-rmks/marisa-bindings/actions/workflows/ci.yaml)
[![Artifacts](https://github.com/juno-rmks/marisa-bindings/actions/workflows/artifacts.yaml/badge.svg)](https://github.com/juno-rmks/marisa-bindings/actions/workflows/artifacts.yaml)
[![Release (TestPyPI)](https://github.com/juno-rmks/marisa-bindings/actions/workflows/release-testpypi.yaml/badge.svg)](https://github.com/juno-rmks/marisa-bindings/actions/workflows/release-testpypi.yaml)
[![Release (PyPI)](https://github.com/juno-rmks/marisa-bindings/actions/workflows/release-pypi.yaml/badge.svg)](https://github.com/juno-rmks/marisa-bindings/actions/workflows/release-pypi.yaml)
[![PyPI version](https://img.shields.io/pypi/v/marisa-bindings.svg)](https://pypi.org/project/marisa-bindings/)
[![Python versions](https://img.shields.io/pypi/pyversions/marisa-bindings.svg)](https://pypi.org/project/marisa-bindings/)
[![License](https://img.shields.io/github/license/juno-rmks/marisa-bindings.svg)](LICENSE)

Thin Python bindings for the C++ **MARISA Trie** library implemented using **SWIG**.

> This is an unofficial binding project and is not affiliated with the original MARISA authors.

## Who is this for?

- You want to use **MARISA Trie** from Python with a **thin wrapper** (keeping the upstream API feel).
- You prefer **upstream-faithful** bindings over a Pythonic re-design.
- You want **reproducible builds** and a pinned upstream source (vendored via git subtree).

## Installation

It is recommended to use a virtual environment to isolate dependencies.

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

## Prebuilt wheel availability

Prebuilt wheels are provided for the following targets:

| OS      | Architecture / ABI | Python    |
| ------- | ------------------ | --------- |
| Linux   | x86_64 (manylinux) | 3.10–3.14 |
| Linux   | i686 (manylinux)   | 3.10–3.14 |
| Linux   | x86_64 (musllinux) | 3.10–3.14 |
| Linux   | i686 (musllinux)   | 3.10–3.14 |
| Windows | x86_64             | 3.10–3.14 |
| Windows | x86                | 3.10–3.14 |
| macOS   | arm64              | 3.10–3.14 |

If your environment is not covered, `pip` will fall back to building from source.
See **Build requirements (source install only)** below.

## Build requirements (source install only)

If a prebuilt wheel is not available for your platform, the package will be built locally.
In that case you need:

- A C++ compiler toolchain
- SWIG ≥ 4.0
- Python development headers

### Linux

```bash
sudo apt install build-essential python3-dev swig
```

Package names may vary depending on your distribution.

### macOS

```bash
xcode-select --install
brew install swig
```

### Windows

Install **Visual Studio Build Tools** (or Visual Studio) with the workload:

- **Desktop development with C++**

## Usage

```python
from marisa_bindings import marisa
```

For a complete example, see:

- `marisa-bindings-sample.py`

## Vendoring policy

This project vendors the upstream MARISA source using **git subtree** to ensure:

- reproducible builds
- long-term stability
- independence from upstream availability

Vendored upstream source lives here:

- `third_party/marisa-trie/upstream/`

Do not modify vendored files directly.
If changes are required, prefer upstream contributions; otherwise keep local patches minimal.

The pinned upstream revision is documented in `VENDORING.md`.

## License

This repository contains multiple components under different licenses:

| Component                            | License                       |
| ------------------------------------ | ----------------------------- |
| Bindings code in this repository     | BSD-2-Clause                  |
| Upstream MARISA Trie (`marisa-trie`) | BSD-2-Clause **or** LGPL-2.1+ |

See `LICENSE` and the vendored upstream license files for details.

## Acknowledgments

Special thanks to the original authors of MARISA Trie for creating the library.
