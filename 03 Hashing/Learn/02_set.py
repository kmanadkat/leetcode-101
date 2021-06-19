################################
#          CREATION
################################
s1 = {10, 20, 30}
print(s1)

s2 = set([20, 30, 40])
print(s2)

s3 = {}
print('expected type set', type(s3))

s4 = set()
print(type(s4))
print(s4)


################################
#          INSERTION
################################
s = {10, 20}
s.add(30)
print(s)

s.add(30)  # adding duplicate items
print(s)

s.update([40, 50])
print(s)
s.update([60, 70], [80, 90])  # inserting multiple list
print(s)


################################
#          REMOVAL
################################
sr = {10, 30, 20, 40}
sr.discard(30)  # Doesnot give error if value not present
print(sr)

sr.remove(20)   # gives error if value not present
print(sr)

sr.clear()
print(sr)
sr.add(50)

del sr


################################
#          OPERATIONS
################################
so = {10, 20, 30}
print(20 in so)
print(50 in so)
print(len(so))

so1 = {2, 4, 6, 8}
so2 = {3, 6, 9}

print('union ', so1 | so2)
print(so1.union(so2))

print('intersecton', so1 & so2)
print(so1.intersection(so2))

print('present in so1, but not present in so2', so1 - so2)
print(so1.difference(so2))

print('symmetric differences, not present in both', so1 ^ so2)


sop1 = {2, 4, 6, 8}
sop2 = {4, 8}

print('disjoint sets:', sop1.isdisjoint(sop2))

print('isSubset:', sop1 <= sop2)
print(sop1.issubset(sop2))

print('proper set:', sop1 < sop2)

print('sop1 is superset of sop2:', sop1 >= sop2)
print(sop1.issuperset(sop2))

print('sop1 is proper superset of sop2:', sop1 > sop2)
