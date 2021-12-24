import urllib.request
import re

nothing = '12345'

while type(nothing) == '':
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing) as response:
        html = response.read()
        html = str(html)
        nothing = re.sub(r'[^0-9]', '', html)
        print(nothing)

