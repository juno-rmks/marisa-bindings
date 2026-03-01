from marisa_bindings import marisa

trie = marisa.Trie()

bad: bool = trie.lookup("apple")
