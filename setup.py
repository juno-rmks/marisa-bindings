import sys
from pathlib import Path

from setuptools import Extension, setup

extra_compile_args = []

if sys.platform == "win32":
    extra_compile_args += ["/std:c++14", "/EHsc"]
else:
    extra_compile_args += ["-std=c++14"]

UPSTREAM = Path("third_party/marisa-trie/upstream")

marisa_sources = [
    *[str(f) for f in (UPSTREAM / "lib/marisa").rglob("*.cc")],
    str(UPSTREAM / "bindings/marisa-swig.i"),
    str(UPSTREAM / "bindings/marisa-swig.cxx"),
]
marisa_include_dirs = [
    str(UPSTREAM / "include"),
    str(UPSTREAM / "lib"),
    str(UPSTREAM / "bindings"),
]

marisa = Extension(
    name="marisa_bindings._marisa",
    sources=marisa_sources,
    include_dirs=marisa_include_dirs,
    language="c++",
    extra_compile_args=extra_compile_args,
    swig_opts=["-c++"],
)

setup(
    ext_modules=[marisa],
)
