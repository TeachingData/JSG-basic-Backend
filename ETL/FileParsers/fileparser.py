from abc import ABC, abstractmethod
import pathlib

class FileParser(ABC):
    def __init__(self):
        self.__file = ""
        self.__data_dir = pathlib.WindowsPath(r'C:\Spark\DataAnalysis\JSG-ETL-basic\ETL\data')
        super().__init__()

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = self.__data_dir / pathlib.Path(file)

    @property
    def directory(self):
        return self.__data_dir

    @directory.setter
    def directory(self, directory: str):
        self.__data_dir = pathlib.WindowsPath(directory)

    def check_file(self):
        return self.__file.exists()

    @abstractmethod
    def parse_file(self):
        pass
