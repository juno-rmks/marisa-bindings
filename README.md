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

- You want to use **MARISA Trie** from Python with a **thin wrapper** that preserves the upstream API.
- You prefer **upstream-faithful bindings** over a Pythonic redesign.
- You want **reproducible builds** with a pinned upstream source (vendored via git subtree).
- You need bindings that behave exactly like the upstream library.

## Design Policy

This project intentionally provides a thin binding layer over MARISA Trie.

Design principles:

- Preserve upstream API behavior
- Avoid adding abstraction layers
- Minimize divergence from upstream
- Ensure reproducible builds

This library is not intended to be a Pythonic wrapper. It prioritizes fidelity to the original MARISA API.

## Installation

A virtual environment is recommended to isolate dependencies.

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

| OS      | Architecture / ABI  | Python    |
| ------- | ------------------- | --------- |
| Linux   | x86_64 (manylinux)  | 3.10–3.14 |
| Linux   | i686 (manylinux)    | 3.10–3.14 |
| Linux   | aarch64 (manylinux) | 3.10–3.14 |
| Linux   | x86_64 (musllinux)  | 3.10–3.14 |
| Linux   | i686 (musllinux)    | 3.10–3.14 |
| Linux   | aarch64 (musllinux) | 3.10–3.14 |
| Windows | x86_64              | 3.10–3.14 |
| Windows | x86                 | 3.10–3.14 |
| macOS   | arm64               | 3.10–3.14 |
| macOS   | x86_64              | 3.10–3.14 |

If your platform is not listed, `pip` will build from source.
See **Build requirements** below.

## Build requirements (source install only)

If a prebuilt wheel is unavailable, local compilation is required:

- C++ compiler toolchain
- Python development headers

> SWIG is not required.
> The binding sources are pre-generated and shipped with the distribution.

### Linux

```bash
sudo apt install build-essential python3-dev
```

Package names may vary depending on your distribution.

### macOS

```bash
xcode-select --install
```

### Windows

Install **Visual Studio Build Tools** with:

- Desktop development with C++

## Usage

```python
from marisa_bindings import marisa
```

See `marisa-bindings-sample.py` for a complete example.

## Benchmarks

Benchmarks are provided under `tests/` and can be executed with **pytest-benchmark**.

### Run

```bash
python -m pip install -U ".[dev]"
python -m pytest -q -m benchmark --benchmark-only
```

Lower is better for latency columns; higher is better for OPS.

### Latest baseline (macOS arm64)

| Benchmark                          | Mean (us) | Median (us) |        OPS |
| ---------------------------------- | --------: | ----------: | ---------: |
| build trie (small)                 | 16,122.46 |   16,029.65 |      62.03 |
| lookup hit (small)                 |    101.38 |      100.83 |   9,863.57 |
| lookup miss (small)                |    413.12 |      411.25 |   2,420.58 |
| common prefix search (small)       |      1.69 |        1.60 | 599,433.23 |
| predictive search (small)          |     11.25 |       11.17 |  88,917.68 |
| lookup hit vs marisa-trie (Cython) |     13.63 |       13.50 |  73,366.88 |

**Environment**

- macOS 15
- Apple Silicon (ARM64)
- Python 3.10

**Notes**

- Results vary depending on CPU scaling, thermal conditions, and background load.

## Vendoring Policy

This project vendors upstream MARISA source using **git subtree** to ensure:

- reproducible builds
- long-term stability
- independence from upstream availability

Vendored upstream source:

```
third_party/marisa-trie/upstream/
```

Do not modify vendored files directly.
If changes are needed, prefer upstream contributions or keep patches minimal.

Pinned upstream revision is documented in `VENDORING.md`.

## License

This repository contains components under different licenses:

| Component            | License                       |
| -------------------- | ----------------------------- |
| Bindings code        | BSD-2-Clause                  |
| Upstream MARISA Trie | BSD-2-Clause **or** LGPL-2.1+ |

See `LICENSE` and vendored license files for details.

## Acknowledgments

Special thanks to the original authors of MARISA Trie.
