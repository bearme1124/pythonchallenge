from collections import Counter

f = open("C:/Users/GOMDURI/source/repos/pythonchallenge/2.ocr/input.txt", 'r')
text = f.read()
#print(text)
f.close()
c = Counter(text)
print(c.most_common())

# equality