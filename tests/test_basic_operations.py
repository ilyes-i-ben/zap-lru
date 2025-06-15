import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lru_cache import LRUCache


class TestLRUCacheBasicOperations(unittest.TestCase):
    
    def setUp(self):
        self.cache = LRUCache(capacity=3)
    
    def test_put_and_get_single_item(self):
        self.cache.put('key1', 'value1')
        result = self.cache.get('key1')
        self.assertEqual(result, 'value1')
    
    def test_get_nonexistent_key(self):
        result = self.cache.get('nonexistent')
        self.assertIsNone(result)
    
    def test_put_multiple_items(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        self.cache.put('key3', 'value3')
        
        self.assertEqual(self.cache.get('key1'), 'value1')
        self.assertEqual(self.cache.get('key2'), 'value2')
        self.assertEqual(self.cache.get('key3'), 'value3')
    
    def test_update_existing_key(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key1', 'updated_value')
        
        result = self.cache.get('key1')
        self.assertEqual(result, 'updated_value')
    
    def test_put_returns_value_on_update(self):
        self.cache.put('key1', 'value1')
        result = self.cache.put('key1', 'updated_value')
        self.assertEqual(result, 'updated_value')


if __name__ == '__main__':
    unittest.main(verbosity=2)
