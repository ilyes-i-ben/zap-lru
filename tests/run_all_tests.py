#!/usr/bin/env python3
"""
Test runner for all LRUCache test files.

This script discovers and runs all test files in the current directory.
"""

import unittest
import sys
import os

def run_all_tests():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    loader = unittest.TestLoader()
    start_dir = test_dir
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\n{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.wasSuccessful()}")
    print(f"{'='*50}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
