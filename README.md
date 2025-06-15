# zap-lru

a small, clean LRU (least recently used) cache in python.

## what's this?

LRU Cache is a data structure that evicts the least recently used items when full. It's implemented using a hashmap + doubly linked list to ensure all get and put operations run in O(1) time.

## Common confusion:
- LRU is a cache => FALSE.
- difference between *LRU* and *LRU cache* :
    - LRU itself (least recently used) is an **eviction policy**... ie) a rule used in order to determine *what* item to "get rid of" when capacity is reached.
    - LRU cache : is a cache implementation that is based on this policy 🙂

## Example

```python
from zaplru import LRUCache

cache = LRUCache(capacity=3)
cache.put("a", "apple")
cache.put("b", "banana")
cache.put("c", "cherry")

print(cache.get("a"))  # "apple" => "a" is MRU (most recently used)
cache.put("d", "date")  # "b" gets evicted (LRU policy..)
print(cache.get("b"))  # None
```