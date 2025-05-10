l1 = ["code", "create", "conquer"]

final = "-".join(l1)
# print(final)

l2 = {"A": 1, "B": 2}

final2 = "-".join(map(str, l2.values()))
# print(final2)


nums = [1, 2, 3]
mapped = map(str, nums)
print(list(mapped))  # ['1', '2', '3']
