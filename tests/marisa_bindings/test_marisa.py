import pytest

from marisa_bindings import marisa


def test_basic_usage_end_to_end(tmp_path: pytest.TempPathFactory):
    # Create a keyset and add some strings to it
    keyset = marisa.Keyset()
    keys = ["cake", "cookie", "ice", "ice-cream"]
    for key in keys:
        keyset.push_back(key)

    # Build a trie from the keyset
    trie = marisa.Trie()
    trie.build(keyset)

    # Basic sanity checks about the constructed trie
    assert trie.num_keys() == 4
    assert trie.num_tries() >= 1
    assert trie.num_nodes() > 0
    assert trie.io_size() > 0

    # Perform exact lookups using an agent
    agent = marisa.Agent()

    agent.set_query("cake")
    assert trie.lookup(agent) is True
    assert agent.query_str() == "cake"
    assert agent.key_id() != marisa.INVALID_KEY_ID

    agent.set_query("cookie")
    assert trie.lookup(agent) is True
    assert agent.query_str() == "cookie"
    assert agent.key_id() != marisa.INVALID_KEY_ID

    # Lookup for a non-existent key (agent)
    agent.set_query("cockoo")
    assert trie.lookup(agent) is False

    # Direct lookup without agent
    assert trie.lookup("ice") != marisa.INVALID_KEY_ID
    assert trie.lookup("ice-cream") != marisa.INVALID_KEY_ID

    # Non-existent key should be INVALID_KEY_ID
    assert trie.lookup("ice-age") == marisa.INVALID_KEY_ID

    # Save the trie to a file and reload it
    dic_path = tmp_path / "sample.dic"
    trie.save(str(dic_path))

    trie2 = marisa.Trie()
    trie2.load(str(dic_path))
    assert trie2.num_keys() == 4

    # Reverse lookup by key ID (collect the strings)
    agent2 = marisa.Agent()
    rev_keys = []
    for key_id in range(4):
        agent2.set_query(key_id)
        trie2.reverse_lookup(agent2)
        rev_keys.append(agent2.key_str())

    # The reverse lookup should return the same set of keys (order may or may not match)
    assert set(rev_keys) == set(keys)

    # Memory-map the trie and perform common prefix search
    trie3 = marisa.Trie()
    trie3.mmap(str(dic_path))

    agent3 = marisa.Agent()
    agent3.set_query("ice-cream soda")

    prefixes = []
    while trie3.common_prefix_search(agent3):
        prefixes.append((agent3.key_str(), agent3.key_id()))

    # For "ice-cream soda", common prefixes should include "ice" and "ice-cream"
    prefix_strings = {k for k, _ in prefixes}
    assert "ice" in prefix_strings
    assert "ice-cream" in prefix_strings

    # Predictive search for "ic" should include "ice" and "ice-cream"
    agent3.set_query("ic")
    preds = []
    while trie3.predictive_search(agent3):
        preds.append((agent3.key_str(), agent3.key_id()))

    pred_strings = {k for k, _ in preds}
    assert "ice" in pred_strings
    assert "ice-cream" in pred_strings
