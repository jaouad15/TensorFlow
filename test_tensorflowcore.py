# test_tensorflowcore.py
"""
Tests for TensorFlowCore module.
"""

import unittest
from tensorflowcore import TensorFlowCore

class TestTensorFlowCore(unittest.TestCase):
    """Test cases for TensorFlowCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TensorFlowCore()
        self.assertIsInstance(instance, TensorFlowCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TensorFlowCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
