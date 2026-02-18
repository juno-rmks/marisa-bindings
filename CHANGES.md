# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4rc1] - 2026-02-18

### Added

- Added support for Python 3.14 wheels via cibuildwheel v3.

### Changed

- Updated GitHub Actions trigger rules to clarify workflow execution conditions.
- Updated wheel build environment to use Python 3.11+ for cibuildwheel execution.

### Fixed

- Fixed an issue where Python 3.14 wheels were not generated during CI builds.

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
