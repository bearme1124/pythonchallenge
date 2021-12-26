"""
peak hell
sounds like pickle
"""
import urllib.request
import pickle

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
text = pickle.loads(html)

# print(text)
# print(len(text)) # 23
# print(len(text[1])) # 5

for i in range(len(text)):
    for j in range(len(text[i])):
        print(text[i][j][0] * text[i][j][1], end = '')
    print('\n')
