import unittest
from lib.package_management import PackageManager

# Unit test class for the PackageManager class
class TestPackageManager(unittest.TestCase):
    
    # Test for the install_package method
    def test_install_package(self):
        manager = PackageManager()
        self.assertIsNone(manager.install_package('dummy-package'))
    
    # Test for the update_package method
    def test_update_package(self):
        manager = PackageManager()
        self.assertIsNone(manager.update_package('dummy-package'))

    # Test for the remove_package method
    def test_remove_package(self):
        manager = PackageManager()
        self.assertIsNone(manager.remove_package('dummy-package'))

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
