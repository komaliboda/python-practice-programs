# Python Set Methods and Operations

# 1. add() - Add one element
numbers = {10, 20, 30}
numbers.add(40)
print("After add:", numbers)


# 2. update() - Add multiple elements
numbers.update([50, 60])
print("After update:", numbers)


# 3. remove() - Remove an element
numbers.remove(60)
print("After remove:", numbers)


# 4. discard() - Remove an element without error if absent
numbers.discard(50)
print("After discard:", numbers)


# 5. pop() - Remove an arbitrary element
removed = numbers.pop()
print("Popped element:", removed)
print("After pop:", numbers)


# 6. clear() - Remove all elements
temp = {10, 20, 30}
temp.clear()
print("After clear:", temp)


# Set operations
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}


# 7. union() - All unique elements
print("Union:", a.union(b))
print("Union using |:", a | b)


# 8. intersection() - Common elements
print("Intersection:", a.intersection(b))
print("Intersection using &:", a & b)


# 9. difference() - Elements only in the first set
print("A - B:", a.difference(b))
print("A - B using -:", a - b)


# 10. symmetric_difference() - Elements that are not common
print("Symmetric difference:", a.symmetric_difference(b))
print("Symmetric difference using ^:", a ^ b)


# 11. issubset() - Check whether one set is inside another
x = {10, 20}
y = {10, 20, 30}

print("Is x a subset of y?", x.issubset(y))


# 12. issuperset() - Check whether one set contains another
print("Is y a superset of x?", y.issuperset(x))


# 13. isdisjoint() - Check whether two sets have nothing in common
p = {10, 20}
q = {30, 40}

print("Are p and q disjoint?", p.isdisjoint(q))