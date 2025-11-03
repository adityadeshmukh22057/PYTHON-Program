# set = {"Virat", "Dhoni", "Rohit", "Rahul", "Rishabh", "Hardik"}
# set2 = {"Shreyas", "Suryakumar", "Bumrah", "siraj", "gill"}
# set3 = {"Axar", "Kuldeep", "Chahal", "Akash"}
# print(set.isdisjoint(set2))
# print(set3.issubset(set2))
# print(set3.issuperset(set2))

# b = set3.update()
# print(b)

# print(set.union(set2, set3))
# print(set.difference(set3))
# a = set.copy()
# a.difference_update(set2)
# print(a)
## intersection
# print(set.intersection(set2))

# x = set3.intersection_update(set2)
# print(x)

# Symmetric Difference
# x = set.symmetric_difference(set2)
# print(x)

# Symmetric Difference Update
#x = set.symmetric_difference_update(set3)

#########################################################################################################################

# a ={11, 34, 54, 7, 23, 45, 67, 89, 90}

# Maximum = max(a)
# Minimum = min(a)
# print(f"Maximum value in the set is: {Maximum}")
# print(f"Minimun value in the set is: {Minimum}")

# a = [1, 4, 6, 7, 3, 2]
# b = [2, 3, 5, 7, 8, 9]
# c = [1, 4, 6, 2, 8, 6]
# print(set(a) & set(b) & set(c))  # Intersection of three sets

a = {1, 4, 6, 7, 3, 2}
b = {2, 3, 5, 7, 8, 9}

# print(a.difference(b))
# print(b.difference(a))

# a.remove(1)
# print(a)

print(b.issubset(a))
print(a.issuperset(b))