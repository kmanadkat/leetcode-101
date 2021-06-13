
l1 = [10, 20, 30, 40, 50]

# Add item at end -> O(1) always
l1.append(30)

# Insert item 15 at index 1 -> right shift rest -> O(n)
l1.insert(1, 15)

# Check if item 15 present in l -> Boolean
print(15 in l1)

# Check how many times item 30 is present in list
print(l1.count(30))

# Find first index of item 30
print(l1.index(30))


################################
#   REMOVING ITEMS FROM LIST
################################

l2 = [10, 20, 30, 40, 50, 60, 70, 80]

# Remove value 20 from list -> Raises ValueError if item not present -> O(n)
l2.remove(20)

# Remove & return last item from list -> O(1)
l2.pop()

# Remove & return item at index 2
l2.pop(2)

# Delete item at index 1
del l2[1]

# Remove items from index 0 to 1 (2-1)
del l2[0:2]


################################
#   LIST FUNCTIONS
################################

l3 = [10, 40, 20, 50]

maxItem = max(l3)

minItem = min(l3)

sumOfAllItems = sum(l3)

reverseList = l3.reverse()

sortedList = l3.sort()  # Ascending order
