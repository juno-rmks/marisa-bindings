"""
Benchmark (sanity check) for marisa-bindings.

- Intended to detect unacceptable regressions / overhead.
- Results vary by machine. Do NOT treat as an absolute comparison.
- CI should skip these benchmarks by default.

Run locally:
    python -m pip install -U ".[dev]" pytest-benchmark
    python -m pytest -q -m benchmark --benchmark-only

Optional comparison target:
    python -m pip install -U marisa-trie
    python -m pytest -q -m benchmark --benchmark-only
"""

# pylint: disable=W0621

import random
import string
from collections.abc import Iterable

import pytest

from marisa_bindings import marisa

pytestmark = pytest.mark.benchmark


def _make_words(
    n: int,
    *,
    seed: int = 0,
    min_len: int = 6,
    max_len: int = 14,
) -> list[str]:
    """
    Generate a sorted list of random lowercase ASCII words.

    Parameters
    ----------
    n : int
        Number of words to generate.
    seed : int, default=0
        Random seed used for deterministic generation.
    min_len : int, default=6
        Minimum word length.
    max_len : int, default=14
        Maximum word length.

    Returns
    -------
    list of str
        Alphabetically sorted list of randomly generated words.

    Notes
    -----
    Sorting ensures deterministic trie structure and stable benchmark results
    across runs.
    """
    rnd = random.Random(seed)
    words: list[str] = []

    for _ in range(n):
        k = rnd.randint(min_len, max_len)
        w = "".join(rnd.choice(string.ascii_lowercase) for _ in range(k))
        words.append(w)

    words.sort()
    return words


def _build_trie(words: Iterable[str]) -> marisa.Trie:
    """
    Build a MARISA trie from an iterable of strings.

    Parameters
    ----------
    words : Iterable[str]
        Input sequence of words used to populate the trie.

    Returns
    -------
    marisa.Trie
        Trie constructed from the provided words.

    Notes
    -----
    Trie construction cost is separated from lookup/search benchmarks to ensure
    measured timings reflect query performance only.
    """
    keyset = marisa.Keyset()

    for w in words:
        keyset.push_back(w)

    trie = marisa.Trie()
    trie.build(keyset)
    return trie


@pytest.fixture(scope="session")
def dataset_small() -> list[str]:
    """
    Provide a small deterministic dataset for benchmarks.

    Returns
    -------
    list of str
        Sorted list of generated words.

    Notes
    -----
    Designed to execute quickly while still exercising trie operations.
    Fixture generation time is excluded from benchmark measurements.
    """
    return _make_words(10_000, seed=1)


@pytest.fixture(scope="session")
def dataset_medium() -> list[str]:
    """
    Provide a medium-sized deterministic dataset for benchmarks.

    Returns
    -------
    list of str
        Sorted list of generated words.

    Notes
    -----
    Used to simulate more realistic workloads while keeping execution time
    reasonable for local runs and CI environments.
    Fixture generation time is excluded from benchmark measurements.
    """
    return _make_words(100_000, seed=2)


@pytest.fixture(scope="session")
def trie_small(dataset_small: list[str]) -> marisa.Trie:
    """
    Construct a trie from the small dataset.

    Parameters
    ----------
    dataset_small : list of str
        Fixture providing input words.

    Returns
    -------
    marisa.Trie
        Trie built from the small dataset.

    Notes
    -----
    Trie construction is performed once per session to avoid affecting
    benchmark timing.
    """
    return _build_trie(dataset_small)


@pytest.fixture(scope="session")
def trie_medium(dataset_medium: list[str]) -> marisa.Trie:
    """
    Construct a trie from the medium dataset.

    Parameters
    ----------
    dataset_medium : list of str
        Fixture providing input words.

    Returns
    -------
    marisa.Trie
        Trie built from the medium dataset.

    Notes
    -----
    This fixture allows benchmarking query performance on a larger structure
    without including build cost in measurements.
    """
    return _build_trie(dataset_medium)


def test_build_trie_small(
    benchmark,
    dataset_small: list[str],
) -> None:
    """
    Benchmark trie construction time on a small dataset.

    Measures the time required to build a trie from a prepared keyset. This
    reflects preprocessing cost rather than query performance.

    Notes
    -----
    Trie construction is typically a one-time cost and is expected to be slower
    than lookup operations.
    """

    def _run() -> None:
        _build_trie(dataset_small)

    benchmark(_run)


def test_lookup_hit_small(
    benchmark,
    trie_small: marisa.Trie,
    dataset_small: list[str],
) -> None:
    """
    Benchmark successful lookup performance.

    Measures the time required to perform exact-match searches where the queried
    key exists in the trie. This represents the best-case lookup scenario.

    Notes
    -----
    This benchmark includes wrapper invocation overhead in addition to native
    lookup execution.
    """
    queries = dataset_small[::200]
    agent = marisa.Agent()

    def _run() -> None:
        for q in queries:
            agent.set_query(q)
            trie_small.lookup(agent)

    benchmark(_run)


def test_lookup_miss_small(
    benchmark,
    trie_small: marisa.Trie,
) -> None:
    """
    Benchmark failed lookup performance.

    Measures the time required to search for a key that does not exist in the
    trie. This represents a worst-case traversal path where the search descends
    until mismatch.

    Notes
    -----
    Miss lookups may be slower than successful ones depending on trie structure.
    """
    misses = [f"zzzz_not_present_{i}" for i in range(200)]
    agent = marisa.Agent()

    def _run() -> None:
        for q in misses:
            agent.set_query(q)
            trie_small.lookup(agent)

    benchmark(_run)


def test_common_prefix_search_small(
    benchmark,
    trie_small: marisa.Trie,
) -> None:
    """
    Benchmark common prefix search performance on a small dataset.

    Measures the execution time of repeated prefix queries against a trie
    constructed from a small set of strings. This test evaluates the speed of
    prefix traversal operations performed inside the native MARISA engine.

    Notes
    -----
    This benchmark focuses on traversal cost and does not include trie
    construction time.
    """
    query = "abcde_fghij_klmno"
    agent = marisa.Agent()

    def _run() -> None:
        agent.set_query(query)

        while trie_small.common_prefix_search(agent):
            pass

    benchmark(_run)


def test_predictive_search_small(
    benchmark,
    trie_small: marisa.Trie,
) -> None:
    """
    Benchmark predictive search performance on a small dataset.

    Measures how fast the trie returns completion candidates for a given prefix.
    This reflects the performance of enumeration-style queries where multiple
    matches are returned.

    Notes
    -----
    Predictive search involves iterative native calls and therefore reflects
    wrapper overhead as well as underlying trie performance.
    """
    prefix = "ab"
    agent = marisa.Agent()

    def _run() -> None:
        agent.set_query(prefix)

        while trie_small.predictive_search(agent):
            pass

    benchmark(_run)


@pytest.fixture(scope="session")
def cython_marisa_trie():
    """
    Provide the optional Cython-based marisa-trie module.

    Returns
    -------
    module
        Imported `marisa_trie` module.

    Raises
    ------
    pytest.skip.Exception
        If the optional dependency is not installed.

    Notes
    -----
    This fixture enables comparative benchmarks between the SWIG-based bindings
    and the Cython implementation. Tests depending on this fixture are skipped
    when the Cython package is unavailable, allowing the suite to run without
    optional dependencies.
    """
    try:
        import marisa_trie  # pylint: disable=C0415
    except Exception:
        pytest.skip("Optional dependency 'marisa-trie' is not installed.")

    return marisa_trie


@pytest.fixture(scope="session")
def cython_trie_small(
    cython_marisa_trie,
    dataset_small: list[str],
):
    """
    Construct a Cython-based MARISA trie using the small dataset.

    Parameters
    ----------
    cython_marisa_trie : module
        Fixture providing the imported `marisa_trie` module.
    dataset_small : list of str
        Fixture supplying input words.

    Returns
    -------
    object
        Trie instance created using the Cython implementation.

    Notes
    -----
    Used exclusively for performance comparison benchmarks against the SWIG-based
    implementation. Construction is performed once per session to avoid including
    build cost in timing measurements.
    """
    return cython_marisa_trie.Trie(dataset_small)


def test_lookup_hit_small_vs_cython(
    benchmark,
    cython_trie_small,
    dataset_small: list[str],
) -> None:
    """
    Benchmark successful lookup performance compared to a Cython binding.

    Measures exact-match lookup time using this implementation and is intended
    to be compared with equivalent benchmarks from a Cython-based binding.

    Notes
    -----
    This test is used for relative comparison only and does not imply functional
    differences between implementations.
    """
    queries = dataset_small[::200]

    def _run() -> None:
        for q in queries:
            _ = cython_trie_small[q]

    benchmark(_run)
