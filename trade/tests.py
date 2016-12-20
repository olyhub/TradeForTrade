from unittest import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEquals(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertEqual(1 + 2, 4)
