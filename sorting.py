import numpy as np



arr = np.array([45, 66, 30, 22])

fa = arr % 2 == 0
new = arr[fa]
print("Filtered array:", new)

# fa = [True, False, True, False]
# new = arr[fa]
# print("Filtered array:", new)

# arr = np.array([[4, 5, 1, 7, 9], [1, 8, 4, 2, 0]])
# print(np.sort(arr))

# at = np.array([3, 7, 1, 9, 3])
# s = np.searchsorted(at, 3)
# print(s)

