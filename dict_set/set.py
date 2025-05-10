my_set = {1, 2, 3}

# Removing an element (safer, no error if not present)
# my_set.discard(8)

# remove the element,error if not present then
# my_set.remove(8)

# removes a random item from the set.
# my_set.pop()
# print(my_set)


set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2  # {1, 2, 3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1 & set2  # {3}
intersection_set = set1.intersection(set2)  # {3}

# Difference
difference_set = set1 - set2  # {1, 2}
difference_set = set1.difference(set2)  # {1, 2}

# Symmetric difference
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}


# PRACTICE SET
