f = open("C:/Users/GOMDURI/source/repos/pythonchallenge/3.equality/source.txt", 'r')
text = f.read()
f.close()

result = ""
for i in range(len(text)-8):
    if text[i].islower() and text[i+1].isupper() and text[i+2].isupper() and text[i+3].isupper() \
    and text[i+4].islower() and text[i+5].isupper() and text[i+6].isupper() and text[i+7].isupper() and text[i+8].islower():
        #print(i)
        result += text[i+4]

print(result)

