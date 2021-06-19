################################
#          CREATION
################################
d = {110: 'abc', 101: 'xyz', 105: 'pqr'}

print(d)

d = {}
d['laptop'] = 40000
d['mobile'] = 15000
d['earphone'] = 1000

print(d)

print(d['mobile'])


################################
#          ACCESS KEY
################################
d = {110: 'abc', 101: 'xyz', 105: 'pqr'}

print(d.get(101))
print(d.get(125))           # Returns None if not found.
print(d.get(125, "NA"))     # Returns default value "NA" if not found

if 125 in d:
    print(d[125])     # Gives error without if
else:
    print("NA")


################################
#         REMOVAL
################################
d = {110: 'abc', 101: 'xyz', 105: 'pqr', 106: 'bcd'}
d[101] = 'wxy'
print(len(d))
print(d)

print('returning and removing 105', d.pop(105))
print('after removing 105', d)

del d[106]
print(d)

d[108] = 'cde'
print('returning and removing last inserted', d.popitem())
