import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lru_cache import LRUCache


class TestLRUCacheIntegration(unittest.TestCase):
    
    def test_large_capacity_cache(self):
        cache = LRUCache(100)
        
        for i in range(100):
            cache.put(f'key{i}', f'value{i}')
        
        for i in range(100):
            self.assertEqual(cache.get(f'key{i}'), f'value{i}')
        
        cache.put('key100', 'value100')
        
        self.assertIsNone(cache.get('key0'))
        self.assertEqual(cache.get('key1'), 'value1')
        self.assertEqual(cache.get('key100'), 'value100')
    
    def test_alternating_operations(self):
        cache = LRUCache(3)
        
        cache.put('A', 1)
        self.assertEqual(cache.get('A'), 1)
        
        cache.put('B', 2)
        self.assertEqual(cache.get('B'), 2)
        self.assertEqual(cache.get('A'), 1)
        
        cache.put('C', 3)
        self.assertEqual(cache.get('C'), 3)
        
        cache.put('D', 4)
        self.assertIsNone(cache.get('B'))
        self.assertEqual(cache.get('A'), 1)
        self.assertEqual(cache.get('C'), 3)
        self.assertEqual(cache.get('D'), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
