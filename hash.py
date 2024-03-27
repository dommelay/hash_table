from collections import namedtuple

class Entry:
  def __init__(self, key, value) -> None:
    self.key = key
    self.value = value

class HashTable:
  def __init__(self) -> None:
    self.size = 1000
    self.table = [[]] * 1000

  def put(self, key, value):
    index = self._hash(key)
    buckets = self.table[index]
    existing = next((e for e in buckets if e.key == key))
  
  def get(self, key):
    index = self._hash(key)
    return self.table[index]
  
  def contains(self, key):
    pass
  
  def _hash(self, key):
    return abs(hash(key)) % self.size