# @Date ：2024/05/20 21:30

class LRUCache:
    pass

if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)  # Cache is {1=1}
    lru_cache.put(2, 2)  # Cache is {1=1, 2=2}
    print(lru_cache.get(1))  # Returns 1 and moves key 1 to the end: Cache is {2=2, 1=1}
    lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, Cache is {1=1, 3=3}
    print(lru_cache.get(2))  # Returns -1 (not found)
    lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, Cache is {3=3, 4=4}
    print(lru_cache.get(1))  # Returns -1 (not found)
    print(lru_cache.get(3))  # Returns 3 and moves key 3 to the end: Cache is {4=4, 3=3}
    print(lru_cache.get(4))  # Returns 4 and moves key 4 to the end: Cache is {3=3, 4=4}
