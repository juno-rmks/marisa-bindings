import os
import subprocess
import sys
from pathlib import Path

import pytest


def _run_mypy(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    """
    Run mypy as a subprocess.

    Notes
    -----
    - We run `python -m mypy` to avoid relying on PATH resolution.
    - `MYPYPATH=src` is set so mypy can find local package sources/stubs.
    """
    env = os.environ.copy()
    env["MYPYPATH"] = str(cwd / "src")

    cmd = [sys.executable, "-m", "mypy", *args]
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


@pytest.mark.typing
def test_mypy_ok_project_root(tmp_path: Path) -> None:
    """
    Ensure mypy accepts a basic typed usage of marisa-bindings.

    This test is intended to validate that `src/marisa_bindings/marisa.pyi`
    (and related typing files) are consistent with the public API.
    """
    # Repository root (tests/..)
    repo_root = Path(__file__).resolve().parents[2]

    # Minimal typed snippet that should pass.
    code = """
from marisa_bindings import marisa

keyset = marisa.Keyset()
keyset.push_back("apple")

trie = marisa.Trie()
trie.build(keyset)

agent = marisa.Agent()
agent.set_query("apple")

hit: bool = trie.lookup(agent)
kid: int = agent.key_id()
ks: str = agent.key_str()

kid2: int = trie.lookup("apple")
kid3: int = trie.lookup("missing")
""".lstrip()

    target = tmp_path / "check_ok.py"
    target.write_text(code, encoding="utf-8")

    # Run mypy against the snippet, using the repository root as cwd
    # so mypy sees the local `src/` layout.
    # We point mypy at the tmp file by absolute path.
    result = _run_mypy(
        "--show-error-codes",
        "--no-error-summary",
        str(target),
        cwd=repo_root,
    )

    if result.returncode != 0:
        raise AssertionError(f"mypy failed:\n{result.stdout}")


@pytest.mark.typing
def test_mypy_ng_project_root(tmp_path: Path) -> None:
    """
    Ensure mypy rejects an intentionally invalid typing usage.

    This acts as a sanity check that the mypy invocation is effective
    (i.e., we are not accidentally skipping analysis).
    """
    repo_root = Path(__file__).resolve().parents[2]

    # Intentionally wrong: `Trie.lookup(str)` should return int (key id),
    # but we assign it to bool to force an error.
    code = """
from marisa_bindings import marisa

trie = marisa.Trie()

bad: bool = trie.lookup("apple")
""".lstrip()

    target = tmp_path / "check_ng.py"
    target.write_text(code, encoding="utf-8")

    result = _run_mypy(
        "--show-error-codes",
        "--no-error-summary",
        str(target),
        cwd=repo_root,
    )

    if result.returncode == 0:
        raise AssertionError("mypy unexpectedly succeeded for an invalid snippet.")
