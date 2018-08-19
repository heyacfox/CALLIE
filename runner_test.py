import unittest
from Machine_Runners import adept_reader_runner


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = adept_reader_runner.AdeptReaderRunner()
        arr.begin_experiment()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
