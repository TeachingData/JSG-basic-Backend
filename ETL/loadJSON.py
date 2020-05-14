from ETL.FileParsers.jsonparser import JSONParser

jp = JSONParser()
jp.file = 'student_poll.json'
jp.parse_file()
jp.print_json()