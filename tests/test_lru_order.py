import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lru_cache import LRUCache


class TestLRUCacheLRUOrder(unittest.TestCase):
    
    def setUp(self):
        self.cache = LRUCache(3)
    
    def test_lru_order_after_mixed_operations(self):
        self.cache.put('A', 1)
        self.cache.put('B', 2)
        self.cache.put('C', 3)
        
        self.cache.get('A')
        
        self.cache.put('B', 22)
        
        self.cache.put('D', 4)
        
        self.assertEqual(self.cache.get('A'), 1)
        self.assertEqual(self.cache.get('B'), 22)
        self.assertIsNone(self.cache.get('C'))
        self.assertEqual(self.cache.get('D'), 4)
    
    def test_get_updates_lru_order(self):
        self.cache.put('A', 1)
        self.cache.put('B', 2)
        self.cache.put('C', 3)
        
        self.cache.get('A')
        self.cache.get('B')
        
        self.cache.put('D', 4)
        
        self.assertEqual(self.cache.get('A'), 1)
        self.assertEqual(self.cache.get('B'), 2)
        self.assertIsNone(self.cache.get('C'))
        self.assertEqual(self.cache.get('D'), 4)
    
    def test_sequential_evictions(self):
        self.cache.put('A', 1)
        self.cache.put('B', 2)
        self.cache.put('C', 3)
        
        self.cache.put('D', 4)
        self.cache.put('E', 5)
        self.cache.put('F', 6)
        
        self.assertIsNone(self.cache.get('A'))
        self.assertIsNone(self.cache.get('B'))
        self.assertIsNone(self.cache.get('C'))
        self.assertEqual(self.cache.get('D'), 4)
        self.assertEqual(self.cache.get('E'), 5)
        self.assertEqual(self.cache.get('F'), 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
