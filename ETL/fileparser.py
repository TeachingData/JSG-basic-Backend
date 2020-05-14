import pathlib

class FileParser:
    def __init__(self):
        self._data_dir = pathlib.WindowsPath(r'C:\Spark\DataAnalysis\ETL-basic\ETL\data')

    def check_file(self, file="survey.txt"):
        file = self._data_dir / file
        return file.exists()
