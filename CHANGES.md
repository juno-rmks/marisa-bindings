# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-02-14

### Changed

- Restructured vendored `marisa-trie` under `third_party/`.
- Documented vendoring policy using git subtree.
- Updated build configuration (`setup.py`, `MANIFEST.in`) to reflect new layout.
- Excluded SWIG-generated artifacts from source control and distributions.
- Improved cross-platform build verification (Linux/macOS/Windows).
- Internal refactoring of vendored dependency management (no API changes).

## [1.0.0] - 2024-08-21

### Added

- First public preview release.
