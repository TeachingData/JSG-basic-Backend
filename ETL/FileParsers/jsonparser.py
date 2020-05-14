from .fileparser import FileParser
import json

class JSONParser(FileParser):
    responses = []

    def parse_file(self):
        with open(self.file, "r") as jd:
            self.responses = json.loads(jd.read())

    def print_json(self):
        for i in self.responses:
            print(f"\nWe are on {i} iteration\n")
            for k in i.keys():
                print(f"The key is {k} with value(s): {i[k]}")
