from .fileparser import FileParser
import json

class JSONParser(FileParser):
    responses = []

    def parse_file(self):
        with open(self.file, "r") as jd:
            # Add call to validator here
            self.responses = json.loads(jd.read())

    def get_responses(self):
        return self.responses

    def print_json(self):
        for i in self.responses:
            print("\n")
            for k in i.keys():
                print(f"The key is {k} with value(s): {i[k]}")
