# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
