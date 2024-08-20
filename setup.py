from pathlib import Path

from setuptools import Extension, setup

marisa_sources = [
    *[str(f) for f in Path('marisa-trie/lib/marisa').rglob('*.cc')],
    str(Path('marisa-trie/bindings/marisa-swig.i')),
    str(Path('marisa-trie/bindings/marisa-swig.cxx')),
]
marisa_include_dirs = [
    str(Path('marisa-trie/include')),
    str(Path('marisa-trie/lib')),
    str(Path('marisa-trie/bindings')),
]

marisa = Extension(
    name='marisa_bindings._marisa',
    sources=marisa_sources,
    include_dirs=marisa_include_dirs,
    language='c++',
    extra_compile_args=['-std=c++14'],
    swig_opts=['-c++'],
)


setup(
    ext_modules=[marisa],
)
