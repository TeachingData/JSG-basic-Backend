import unittest
from ETL.FileParsers.jsonparser import JSONParser

# TODO: Add mock of json.loads & open

class TestJSONParser(unittest.TestCase):
    jp = JSONParser()

    def test_check_file(self):
        self.jp.file = "student_poll.json"
        assert self.jp.check_file() is True

    def test_get_responses(self):
        test_dict = {'grade': 'freshman', 'TA': False}
        self.jp.responses = [{'grade': 'freshman', 'TA': False}, {'grade': 'sophomore', 'TA': False}]
        self.assertDictEqual(self.jp.get_responses()[0], test_dict)
