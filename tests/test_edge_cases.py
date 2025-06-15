import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lru_cache import LRUCache


class TestLRUCacheEdgeCases(unittest.TestCase):
    
    def test_zero_capacity(self):
        cache = LRUCache(0)
        cache.put('key1', 'value1')
        result = cache.get('key1')
        self.assertIsNone(result)
    
    def test_single_capacity(self):
        cache = LRUCache(1)
        cache.put('key1', 'value1')
        self.assertEqual(cache.get('key1'), 'value1')
        
        cache.put('key2', 'value2')
        self.assertIsNone(cache.get('key1'))
        self.assertEqual(cache.get('key2'), 'value2')
    
    def test_repeated_gets(self):
        cache = LRUCache(2)
        cache.put('key1', 'value1')
        
        for _ in range(5):
            result = cache.get('key1')
            self.assertEqual(result, 'value1')
    
    def test_repeated_puts_same_key(self):
        cache = LRUCache(2)
        
        for i in range(5):
            cache.put('key1', f'value{i}')
        
        result = cache.get('key1')
        self.assertEqual(result, 'value4')
    
    def test_different_data_types(self):
        cache = LRUCache(3)
        
        cache.put('string_key', 'string_value')
        cache.put(123, 'numeric_key')
        cache.put('list_value', [1, 2, 3])
        
        self.assertEqual(cache.get('string_key'), 'string_value')
        self.assertEqual(cache.get(123), 'numeric_key')
        self.assertEqual(cache.get('list_value'), [1, 2, 3])
    
    def test_none_values(self):
        cache = LRUCache(2)
        cache.put('key1', None)
        
        result = cache.get('key1')
        self.assertIsNone(result)
        
        cache.put('key2', 'value2')
        cache.put('key3', 'value3')
        
        self.assertIsNone(cache.get('key1'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
