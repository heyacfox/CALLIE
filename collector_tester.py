import unittest
from Collectors import gutenberg_collector


class MyTestCase(unittest.TestCase):
    def test_something(self):
        gc = gutenberg_collector.GutenbergCollector()
        gc.get_content_at_indexes()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
