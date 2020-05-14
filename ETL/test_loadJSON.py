import pytest
from ETL.FileParsers.jsonparser import JSONParser

# This will be replaced by specific fileParser unit tests (as it will be the abstract)
def test_check_file():
    jp = JSONParser()
    jp.file = "student_poll.json"
    assert jp.check_file() is True
