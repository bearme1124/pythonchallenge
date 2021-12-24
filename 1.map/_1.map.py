str_line = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

"""
new_str = ""
for i in range(len(str_line)):
    s = ord(str_line[i])
    if chr(s) == " " or chr(s) == ".":
        new_str += str_line[i]
    elif (s + 2) > ord("z"):
        new_str += chr(s + 2 - ord("z") + ord("a") - 1)
    else:
        new_str += chr(s + 2)
print(new_str)
"""
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str_line.maketrans(intab, outtab)
print(str_line.translate(trantab))

str_url = "map"
trantab = str_url.maketrans(intab, outtab)
print(str_url.translate(trantab))

