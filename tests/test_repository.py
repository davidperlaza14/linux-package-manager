import unittest
from lib.repository import Repository


# Unit test class for the Repository class
class TestRepository(unittest.TestCase):
    
    # Test for the update method
    def test_update(self):
        repo = Repository()
        self.assertIsNone(repo.update())


# Run the unit tests
if __name__ == '__main__':
    unittest.main()