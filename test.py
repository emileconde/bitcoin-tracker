import unittest
from utils import*

"""TEST CASES:
-Check that the response of the request isn't null
-Check that the parser returns a non null dictionary
-Check that parse_json returns when an empty response is passed
as a parameter.
"""

class TestFileName(unittest.TestCase):
    def test_is_response_null(self):
        self.assertTrue()

    def test_function2(self):
        self.assertEqual(function2(2,1), 3)
        self.assertEqual(function2(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()