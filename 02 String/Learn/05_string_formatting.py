
name = "krupesh"
course = "Python Course"


# Method 1 - Using %
s1 = "Welcome %s to the %s" % (name, course)

# Method 2 - Using Format Function
s2 = "Welcome {0} to the {1}".format(name, course)

# Method 3 - Using f-string
s3 = f"Welcome {name} to the {course}"

print(s1)
print(s2)
print(s3)


# F String Examples
a = 10
b = 20
print(f"{a} + {b} = {a + b}")

s1 = "ABC"
s2 = "abc"
print(f"Lower case of {s1} is: {s1.lower()}")
print(f"Upper case of {s2} is: {s2.upper()}")
