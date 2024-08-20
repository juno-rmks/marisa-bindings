"""
This script showcases the basic usage of the `marisa-bindings` library,
which provides bindings for the MARISA trie. It covers key insertion,
trie construction, querying (including exact, prefix, and predictive searches),
and saving/loading the trie.
"""

from marisa_bindings import marisa

# Create a keyset and add some strings to it
keyset = marisa.Keyset()
keys = ["cake", "cookie", "ice", "ice-cream"]

for key in keys:
    keyset.push_back(key)

# Build a trie from the keyset
trie = marisa.Trie()
trie.build(keyset)

# Print information about the constructed trie
print(f"no. keys: {trie.num_keys()}")
print(f"no. tries: {trie.num_tries()}")
print(f"no. nodes: {trie.num_nodes()}")
print(f"size: {trie.io_size()}")

# Perform exact lookups using an agent
agent = marisa.Agent()

for key in ["cake", "cookie"]:
    agent.set_query(key)
    trie.lookup(agent)
    print(f"{agent.query_str()}: {agent.key_id()}")

# Lookup for a non-existent key
agent.set_query("cockoo")

if not trie.lookup(agent):
    print(f"{agent.query_str()}: not found")

# Directly lookup keys without using an agent
print(f"ice: {trie.lookup('ice')}")
print(f"ice-cream: {trie.lookup('ice-cream')}")

# Check if a non-existent key returns INVALID_KEY_ID
if trie.lookup("ice-age") == marisa.INVALID_KEY_ID:
    print("ice-age: not found")

# Save the trie to a file and reload it
trie.save("sample.dic")
trie.load("sample.dic")

# Perform reverse lookups by key ID
for key_id in range(4):
    agent.set_query(key_id)
    trie.reverse_lookup(agent)
    print(f"{agent.query_id()}: {agent.key_str()}")

# Memory-map the trie from the file and perform common prefix search
trie.mmap("sample.dic")
agent.set_query("ice-cream soda")

while trie.common_prefix_search(agent):
    print(f"{agent.query_str()}: {agent.key_str()} ({agent.key_id()})")

# Perform predictive search
agent.set_query("ic")

while trie.predictive_search(agent):
    print(f"{agent.query_str()}: {agent.key_str()} ({agent.key_id()})")
