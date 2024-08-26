"""
    HashTable implementation that handles collisions
    using Chaining approach
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.bins = [None for i in range(self.size)]


def HashTableInsert(ht: HashTable, key: str, value: any):
    hash_value = hash(key) % ht.size
    print(f"Inserting: {key}, using hash value of: {hash_value}")

    if ht.bins[hash_value] is None:
        ht.bins[hash_value] = Node(key, value)
        return

    # key already exists in the table
    current = ht.bins[hash_value]
    while current.key != key and current.next != None:
        current = current.next

    if current.key == key:
        current.value = value
    else:
        current.next = Node(key, value)


def HashTableLookUp(ht: HashTable, key: str) -> any:
    hash_value = hash(key) % ht.size
    print(f"Looking up: {key} using hash value of: {hash_value}")

    if ht.bins[hash_value] is None:
        return None

    current = ht.bins[hash_value]
    while current.key != key and current.next != None:
        current = current.next

    if current.key == key:
        return current.value

    return None

def HashTableRemove(ht: HashTable, key: str) -> Node:
    hash_value = hash(key) % ht.size
    print(f"Removing key: {key} using hash value of: {hash_value}")

    if ht.bins[hash_value] is None:
        return None

    current = ht.bins[hash_value]
    last = None
    while current.key != key and current.next != None:
        last = current
        current = current.next

    if current.key == key:
        if last is not None:
            last.next = current.next
        else:
            ht.bins[hash_value] = current.next

        return current

    return None

if __name__ == "__main__":
    ht = HashTable(10)

    HashTableInsert(ht, "Moises", "Foo Bar")
    HashTableInsert(ht, "Lilo", "Baz Zaz")
    print("--" * 10)
    print(f"Looking up value of Moises: {HashTableLookUp(ht, 'Moises')}")
    print(f"Looking up value of Lilo: {HashTableLookUp(ht, 'Lilo')}")
    print("--" * 10)
    HashTableRemove(ht, "Moises")
    print(f"Looking up value of Moises: {HashTableLookUp(ht, 'Moises')}")
    print("--" * 10)
