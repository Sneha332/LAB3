import re

#Check if the string starts with "The" and ends with "Spain":
txt1="abc123"
txt2="456xyz"
txt3="a_b c!"
txt4="789abcxyz"
txt5="abc xyz"
txt6="no_digits_here"


x11 = re.findall("\d", txt1)
x12 = re.findall("\d", txt2)
x13= re.findall("\d", txt3)
x14 = re.findall("\d", txt4)
x15 = re.findall("\d", txt5)
x16 = re.findall("\d", txt6)

print("digit characters:",x11)
print("digit characters:",x12)
print("digit characters:",x13)
print("digit characters:",x14)
print("digit characters:",x15)
print("digit characters:",x16)

x21 = re.findall("\D", txt1)
x22 = re.findall("\D", txt2)
x23= re.findall("\D", txt3)
x24 = re.findall("\D", txt4)
x25 = re.findall("\D", txt5)
x26 = re.findall("\D", txt6)

print("Non digit Characters:",x21)
print("Non digit Characters:",x22)
print("Non digit Characters:",x23)
print("Non digit Characters:",x24)
print("Non digit Characters:",x25)
print("Non digit Characters:",x26)

x31 = re.findall("\D", txt1)
x32 = re.findall("\D", txt2)
x33= re.findall("\D", txt3)
x34 = re.findall("\D", txt4)
x35 = re.findall("\D", txt5)
x36 = re.findall("\D", txt6)

print("Word Characters:",x31)
print("Word Characters:",x32)
print("Word Characters:",x33)
print("Word Characters:",x34)
print("Word Characters:",x35)
print("Word Characters:",x36)

x41 = re.findall("\w", txt1)
x42 = re.findall("\w", txt2)
x43= re.findall("\w", txt3)
x44 = re.findall("\w", txt4)
x45 = re.findall("\w", txt5)
x46 = re.findall("\w", txt6)

print("NOn Word Characters:",x41)
print("Non Word Characters:",x42)
print("Non Word Characters:",x43)
print("Non Word Characters:",x44)
print("Non Word Characters:",x45)
print("Non Word Characters:",x46)

x51 = re.findall("\W", txt1)
x52 = re.findall("\W", txt2)
x53= re.findall("\W", txt3)
x54 = re.findall("\W", txt4)
x55 = re.findall("\W", txt5)
x56 = re.findall("\W", txt6)

print(x51)
print(x52)
print(x53)
print(x54)
print(x55)
print(x56)

x61 = re.findall("\W", txt1)
x62 = re.findall("\W", txt2)
x63= re.findall("\W", txt3)
x64 = re.findall("\W", txt4)
x65 = re.findall("\W", txt5)
x66 = re.findall("\W", txt6)

print(x61)
print(x62)
print(x63)
print(x64)
print(x65)
print(x66)
x71 = re.findall("\s", txt1)
x72 = re.findall("\s", txt2)
x73= re.findall("\s", txt3)
x74 = re.findall("\s", txt4)
x75 = re.findall("\s", txt5)
x76 = re.findall("\s", txt6)
print(x71)
print(x72)
print(x73)
print(x74)
print(x75)
print(x76)

x81 = re.findall("\S", txt1)
x82 = re.findall("\S", txt2)
x83= re.findall("\S", txt3)
x84 = re.findall("\S", txt4)
x85 = re.findall("\S", txt5)
x86 = re.findall("\S", txt6)

print(x81)
print(x82)
print(x83)
print(x84)
print(x85)
print(x86)

x91 = re.findall("^abc", txt1)
x92 = re.findall("^abc", txt2)
x93= re.findall("^abc", txt3)
x94 = re.findall("^abc", txt4)
x95 = re.findall("^abc", txt5)
x96 = re.findall("^abc", txt6)
print(x91)
print(x92)
print(x93)
print(x94)
print(x95)
print(x96)

x01 = re.findall("xyz$", txt1)
x02 = re.findall("xyz$", txt2)
x03= re.findall("xyz$", txt3)
x04 = re.findall("xyz$", txt4)
x05 = re.findall("xyz$", txt5)
x06 = re.findall("xyz$", txt6)

print(x01)
print(x02)
print(x03)
print(x04)
print(x05)
print(x06)




