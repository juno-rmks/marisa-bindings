# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.6] - 2026-03-10

### Added

- Added PEP 561 type support (py.typed).
- Introduced marisa.pyi type stubs for the public API.
- Added mypy-based typing tests (pytest -m typing).
- Added Linux `aarch64` wheel builds.
- Added macOS `x86_64` wheel builds.

### Changed

- Refined type definitions and overloads for improved static type checking.
- Documented macOS `x86_64` wheel support in README.

## [1.0.5] - 2026-02-22

### Changed

- Switched to vendored SWIG-generated binding sources, removing the build-time SWIG dependency.
- Updated packaging configuration to use pre-generated wrapper sources instead of `.i` files.
- Adjusted MANIFEST and build configuration to exclude upstream SWIG artifacts.
- Clarified vendoring policy for bindings layer in documentation.

### Removed

- Removed SWIG from build-system requirements.
- Removed reliance on system SWIG during wheel and sdist builds.

## [1.0.4] - 2026-02-22

### Added

- Added support for building Python 3.14 wheels.
- Added benchmark test suite based on pytest-benchmark.
- Added benchmark results section to README.

### Changed

- Upgraded to cibuildwheel v3.
- Updated wheel build environment to use Python 3.11 or later for running cibuildwheel.
- Refined GitHub Actions trigger rules to clarify workflow execution conditions.
- Improved README structure and documentation clarity.

### Fixed

- Resolved an issue where Python 3.14 wheels were not generated in CI builds.

## [1.0.3] - 2026-02-16

### Fixed

- Fix PyPI release pipeline by validating distributions during the build job
  (avoid toolchain differences at publish time).

## [1.0.2] - 2026-02-16

### Changed

- Align project summary/description with README.

### Fixed

- Fix package metadata for PyPI (license-file / license handling) and ensure
  LICENSE is included in sdist.

## [1.0.1] - 2026-02-15

### Changed

- Vendored MARISA source moved into structured `third_party/marisa-trie/upstream/` layout.
- Build configuration updated to support platform-specific compiler flags.

### Fixed

- Windows build compatibility improvements.

## [1.0.0] - 2024-08-21

### Added

- First public preview release.
