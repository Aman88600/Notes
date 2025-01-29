# Used to search for patterns within strings
import re

text = "Hello, World!"

print(re.search("^H...o$", text))