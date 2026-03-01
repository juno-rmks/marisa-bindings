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
    - Runs `python -m mypy` to avoid relying on PATH resolution.
    - Sets `MYPYPATH=src` so mypy can find local package sources/stubs.
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


def _repo_root() -> Path:
    """
    Return repository root path.

    Notes
    -----
    Assumes this file is located at `tests/marisa_bindings/test_typing_mypy.py`.
    """
    return Path(__file__).resolve().parents[2]


def _typing_snippet(name: str) -> Path:
    """
    Return path to a typing snippet file.

    Parameters
    ----------
    name:
        Snippet file name under `tests/marisa_bindings/typing/`, e.g. `ok_basic.py`.
    """
    return Path(__file__).resolve().parent / "typing" / name


@pytest.mark.typing
def test_mypy_ok_project_root() -> None:
    """
    Ensure mypy accepts basic typed usage of marisa-bindings.

    This validates that `src/marisa_bindings/marisa.pyi` matches the public API
    surface of `marisa_bindings.marisa`.
    """
    repo_root = _repo_root()
    target = _typing_snippet("ok_basic.py")
    result = _run_mypy(
        "--show-error-codes",
        "--no-error-summary",
        "--pretty",
        str(target),
        cwd=repo_root,
    )

    if result.returncode != 0:
        raise AssertionError(f"mypy failed:\n{result.stdout}")


@pytest.mark.typing
def test_mypy_ng_project_root() -> None:
    """
    Ensure mypy rejects an intentionally invalid typing usage.

    This acts as a sanity check that the mypy invocation is effective.
    """
    repo_root = _repo_root()
    target = _typing_snippet("ng_basic.py")
    result = _run_mypy(
        "--show-error-codes",
        "--no-error-summary",
        "--pretty",
        str(target),
        cwd=repo_root,
    )

    if result.returncode == 0:
        raise AssertionError("mypy unexpectedly succeeded for an invalid snippet.")
