import pytest
from ETL.loadJSON import FileParser

# This will be replaced by specific fileParser unit tests (as it will be the abstract)
def test_check_file():
    fp = FileParser()
    assert fp.check_file("student_poll.json") is True