l = [10, 20, 30, 40, 50]

# Prints from index 0 to index 4 (5-1) with increment of 2
print(l[0:5:2])

# Prints from index 0 to 3 (4-1)
print(l[:4])

# Prints from index 2 to end
print(l[2:])

# Start 0 end 3
print(l[1:4])

# Start last index; end zeroth index; goes backward -> -1 step
print(l[-1:-6:-1])

# Sames as above, reversed list
print(l[::-1])

# Print entire list
print(l[:])
