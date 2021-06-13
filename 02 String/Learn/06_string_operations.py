
s1 = "geeksforgeeks"
s2 = "geeks"

# Check If s2 is substring of s1
s2SubStrS1 = s2 in s1
print(s2SubStrS1)

# Concatenation
s3 = s1 + s2
print(s3)


# Find First Occurence Index of Substring s2
# NOTE : s2 must be Substring -> else gives an error
print(s1.index(s2))


# Find Last Occurence Index of Substring s2
# NOTE : s2 must be Substring -> else gives an error
print(s1.rindex(s2))


# Find First Occurence Index of Substring s2 in range
# NOTE : s2 must be Substring -> else gives an error
print(s1.rindex(s2, 1, len(s1)))


# String Case
sc1 = "geeks"

sc2 = sc1.upper()
sc3 = sc2.lower()

print(sc2)
print(sc3)

print(sc2.isupper())
print(sc3.islower())


# String Position
sp1 = "GeeksForGeeks Python Course"
print(sp1.startswith("Geeks"))
print(sp1.endswith("Course"))

# Second parameter is start index
print(sp1.startswith("Geeks", 1))

# Third parameter is end index + 1
print(sp1.startswith("Geeks", 8, len(sp1)))


# String Splitting & joinning
spj1 = "Geeks For Geeks"
spj2 = "Geeks, For, Geeks"

print(spj1.split())
print(spj2.split(", "))

l1 = ["geeks", "for", "geeks", "python"]
print(" ".join(l1))
print(", ".join(l1))


# String Strip -> Remove Characters from corners
ss = "----python strings----"
print(ss.strip('-'))
print(ss.lstrip('-'))
print(ss.rstrip('-'))


# String Find Method
ssf = "Geeks for geeks python course"
print(ssf.find("Geeks"))
print(ssf.find("Python"))
