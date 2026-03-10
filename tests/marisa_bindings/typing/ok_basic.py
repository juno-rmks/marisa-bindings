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
