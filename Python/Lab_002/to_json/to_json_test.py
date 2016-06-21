import unittest
import json
import to_json


class Test_to_json(unittest.TestCase):

    def setUp(self):
        self.obj = {'one': 1, 'two': [1, 2, 3],
                    'three': True, 'four': None}
        self.obj1 = [1, 'aaa', {'python': 'cool'}]

    def test(self):
        self.assertEqual(to_json.to_json(self.obj), json.dumps(self.obj))

    def test2(self):
        self.assertEqual(to_json.to_json(self.obj1), json.dumps(self.obj1))

if __name__ == "__main__":
    unittest.main()