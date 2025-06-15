import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lru_cache import LRUCache


class TestLRUCacheEviction(unittest.TestCase):
    
    def setUp(self):
        self.cache = LRUCache(2)
    
    def test_eviction_on_capacity_exceeded(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        self.cache.put('key3', 'value3')
        
        self.assertIsNone(self.cache.get('key1'))
        self.assertEqual(self.cache.get('key2'), 'value2')
        self.assertEqual(self.cache.get('key3'), 'value3')
    
    def test_multiple_evictions(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        self.cache.put('key3', 'value3')
        self.cache.put('key4', 'value4')
        
        self.assertIsNone(self.cache.get('key1'))
        self.assertIsNone(self.cache.get('key2'))
        self.assertEqual(self.cache.get('key3'), 'value3')
        self.assertEqual(self.cache.get('key4'), 'value4')
    
    def test_eviction_order_with_gets(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        
        self.cache.get('key1')
        
        self.cache.put('key3', 'value3')
        
        self.assertEqual(self.cache.get('key1'), 'value1')
        self.assertIsNone(self.cache.get('key2'))
        self.assertEqual(self.cache.get('key3'), 'value3')
    
    def test_eviction_order_with_updates(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        
        self.cache.put('key1', 'updated_value1')
        
        self.cache.put('key3', 'value3')
        
        self.assertEqual(self.cache.get('key1'), 'updated_value1')
        self.assertIsNone(self.cache.get('key2'))
        self.assertEqual(self.cache.get('key3'), 'value3')


if __name__ == '__main__':
    unittest.main(verbosity=2)
