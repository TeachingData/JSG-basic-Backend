import requests

""" Simple script to demonstrate how HTTP requests work (to 
    demonstrating TCP/IP) using Python. Such as "3-way handshake",
    get/post requests, byte encoding (and problems such as Latin),
    and the first step of scraping and data mining.
"""

response = requests.get("https://www.gutenberg.org/files/59824/59824-0.txt", stream=True)

""" As learned in class, this pulls over some encoding issues - here due to Python
    ... single apostorphe can be a pain to new developers. 
    So let's check the encoding.
"""

print(response.encoding) 
#On windows: ISO, Linux: ?, Apple: ? - in class try this
#For now (we'll look at bytes later) let's just set it to utf-8
response.encoding = 'utf-8'

""" There are better ways to achieve this but we need to check 2 things so:
    Selected poems happens twice so we'll set 2 flags (for simplicity)
        * start_flag is TRUE until we hit start of poems ("SELECTED POEMS")
        * BUt this happens twice so we also set a counter to 1 (i.e. happened once already)
    We need to check if each line is empty (the strip() if statement)
    Then we just print it
"""
    
start_flag = True
start_counter = 0

# for chunk in r.iter_content(chunk_size=1000000): #Explain chunk & stream in class
for curline in response.iter_lines():
    if curline.strip(): #ignore blank lines ("" = False)
        if start_flag: #skip every line until end
            if curline.startswith(b'SELECTED POEMS'):
                if start_counter == 1:
                    start_flag = False
                else:
                    start_counter = 1
        else:
            if not curline.startswith(b'End of the Project Gutenberg'): 
              #make byte literal using b - prepare to answer why in class
                print(curline)
            else:
                break
